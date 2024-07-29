#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/23
# @Author  : yanxiaodong
# @File    : train_component.py
"""
import os
import json
from argparse import ArgumentParser
import shutil
from gaea_tracker import ExperimentTracker
from bcelogger.base_logger import setup_logger
from windmillmodelv1.client.model_api_model import parse_model_name
from windmillmodelv1.client.model_api_model import ModelName
from windmillmodelv1.client.model_api_modelstore import parse_modelstore_name
from windmillclient.client.windmill_client import WindmillClient
import bcelogger
from gaea_operator.utils import find_upper_level_folder

from gaea_operator.dataset import CocoDataset
from gaea_operator.config import PPYOLOEPLUSMConfig
from gaea_operator.metric.types.metric import LOSS_METRIC_NAME, \
    MAP_METRIC_NAME, \
    AP50_METRIC_NAME, \
    AR_METRIC_NAME, \
    BOUNDING_BOX_MEAN_AVERAGE_PRECISION_METRIC_NAME
from gaea_operator.trainer import Trainer
from gaea_operator.model import Model
from gaea_operator.metric import get_score_from_file
from gaea_operator.utils import write_file
import json
import yaml
import os

NX_ANNOTATION_TYPE_DET = 'detect'
NX_ANNOTATION_TYPE_CLS = 'classify'
NX_ANNOTATION_TYPE_SEG = 'segment'

NX_SPLIT_CHAR = ' '

def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK"))
    parser.add_argument("--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK"))
    parser.add_argument("--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT"))
    parser.add_argument("--project-name", type=str, default=os.environ.get("PROJECT_NAME"))
    parser.add_argument("--scene", type=str, default=os.environ.get("SCENE"))
    parser.add_argument("--public-model-store",
                        type=str,
                        default=os.environ.get("PUBLIC_MODEL_STORE", "workspaces/public/modelstores/public"))
    parser.add_argument("--tracking-uri", type=str, default=os.environ.get("TRACKING_URI"))
    parser.add_argument("--experiment-name", type=str, default=os.environ.get("EXPERIMENT_NAME"))
    parser.add_argument("--experiment-kind", type=str, default=os.environ.get("EXPERIMENT_KIND"))
    parser.add_argument("--train-dataset-name",
                        type=str,
                        default=os.environ.get("TRAIN_DATASET_NAME"))
    parser.add_argument("--val-dataset-name", type=str, default=os.environ.get("VAL_DATASET_NAME"))
    parser.add_argument("--base-train-dataset-name",
                        type=str,
                        default=os.environ.get("BASE_TRAIN_DATASET_NAME"))
    parser.add_argument("--base-val-dataset-name", type=str, default=os.environ.get("BASE_VAL_DATASET_NAME"))
    parser.add_argument("--model-name", type=str, default=os.environ.get("MODEL_NAME"))
    parser.add_argument("--model-display-name",
                        type=str,
                        default=os.environ.get("MODEL_DISPLAY_NAME"))
    parser.add_argument("--advanced-parameters",
                        type=str,
                        default=os.environ.get("ADVANCED_PARAMETERS", "{}"))

    parser.add_argument("--output-model-uri", type=str, default=os.environ.get("OUTPUT_MODEL_URI"))
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))
    parser.add_argument("--train_config_params_uri", type=str, default=os.environ.get("TRAIN_CONFIG_PARAMS_URI"))

    args, _ = parser.parse_known_args()

    return args

def _delete_file_name_prefix(path_str):
    """
    删除文件名前缀，返回去掉前缀的路径字符串。如果路径字符串不是以指定的前缀开头，则返回None。
    
    Args:
        path_str (str): 包含文件名的路径字符串，可能以bos:/、s3:/或/开头。
    
    Returns:
        Union[str, None]: 去掉前缀后的路径字符串，如果路径字符串不是以指定的前缀开头，则返回None。
    """
    prefix = ['bos:/', 's3:/', '/']
    for _, p in enumerate(prefix):
        if path_str.startswith(p):
            abs_path = path_str[len(p): ]
            if not abs_path.startswith('/'):
                abs_path = '/' + abs_path
            return abs_path
    return None

def _cvt_2_abs_path(path_str, abs_work_path, default_prefix=None, abs_work_folders=None, abs_work_default_folders=None):
    """
    将相对路径转换为绝对路径，如果不是bos/s3的路径则会抛出ValueError。
    
    Args:
        path_str (str): 需要转换的路径字符串，可以是相对路径或者绝对路径。
            - 若路径字符串以bos://开头，则认为是bos路径，不进行处理；
            - 若路径字符串以s3://开头，则认为是s3路径，不进行处理；
            - 否则，认为是相对路径，会根据abs_work_path参数进行转换。
        abs_work_path (str): 工作目录的绝对路径，用于处理相对路径。
        default_prefix (str): 默认的前缀，用于处理相对路径。
        abs_work_folders (List[str]): 工作目录的所有子目录文件名，用于处理相对路径。
        abs_work_default_folders (List[str]): 工作目录的默认子目录文件名，用于处理相对路径。
    
    Returns:
        str: 返回一个绝对路径字符串。
    
    Raises:
        ValueError: 当路径字符串不是bos/s3路径且无法通过abs_work_path转换成绝对路径时，会抛出ValueError异常。
    """
    # 1. judge bos/s3
    abs_path = _delete_file_name_prefix(path_str)
    if abs_path is not None:
        return abs_path
    
    # 2. relative path -> abs path
    top_folder = path_str.split('/')[0]
    default_prefix = default_prefix if default_prefix else 'images'

    # 2.1 search relative path top folder from abs_work_path
    ## 最高优先级为外部指定输入
    if abs_work_folders is not None:
        folders = abs_work_folders
    else:
        ## 如果存在 abs_work_path 赋值 listdir 结果，否则赋值 []
        if os.path.exists(abs_work_path):
            folders = os.listdir(abs_work_path)
        else:
            folders = []
    
    ## 最高优先级为外部指定输入
    if abs_work_default_folders is not None:
        abs_work_default_folders = abs_work_default_folders
    else:
        ## 如果存在 default_prefix 赋值 listdir 结果，否则赋值 []
        abs_work_default_path = os.path.join(abs_work_path, default_prefix)
        if os.path.exists(abs_work_default_path):
            abs_work_default_folders = os.listdir(abs_work_default_path)
        else:
            abs_work_default_folders = []

    if top_folder in folders:
        return os.path.join(abs_work_path, path_str)
    elif default_prefix in folders and top_folder in abs_work_default_folders:
        return os.path.join(abs_work_path, default_prefix, path_str)
    else:
        raise ValueError("relativate path file is invalid, please check. path: {} work_path: {}".format(path_str,
                                                                                                        abs_work_path))

def _retrive_path(path, exts, prefix):
        """
        从指定路径中递归搜索，返回指定扩展名的文件列表

        Args:
        path (str): 指定的文件目录路径
        exts (list[str]): 文件扩展名列表

        Returns:
        list[str]: 返回包含文件路径的列表

        """
        aim_files = []
        n = 0
        for home, dirs, files in os.walk(path):
            for _, f in enumerate(files):
                if f.split('.')[-1] in exts and not f.startswith(".") and f.startswith(prefix):
                    w_name = os.path.join(home, f)
                    n += 1
                    bcelogger.info("FIND" + str(n) + ":" + w_name)
                    aim_files.append(w_name)

        return aim_files

def _modify_detection_annotations(
        src_name, dst_path, abs_work_path, abs_work_folders, abs_work_default_folders, all_image_folders):
    """
    修改检测标注文件，将相对路径转换为绝对路径。
    
    Args:
        src_name (str): 原始标注文件名，包含路径信息。
        dst_path (str): 目标保存路径。
        abs_work_path (str): 工作目录的绝对路径。
        abs_work_folders (list[str]): 工作目录的所有子目录文件名。
        abs_work_default_folders (list[str]): 工作目录的默认子目录文件名。
        all_image_folders (set[str]): 工作目录下的所有图片文件夹
    
    Returns:
        str: 返回已经修改后的标注文件名，包含完整路径信息。
        
    Raises:
        None.
    """
    json_data = json.load(open(src_name, "r"))
    images = json_data["images"]
    bcelogger.info(f"Parse annotation file {src_name}, image num is {len(images)}")
            
    for img in images:
        img["file_name"] = _cvt_2_abs_path(
                img["file_name"], abs_work_path, 'images', abs_work_folders, abs_work_default_folders)
        all_image_folders.add(os.path.dirname(img["file_name"]))
    
    dst_name = os.path.join(dst_path, src_name.split('/')[-1])
    with open(dst_name, "w") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    
    bcelogger.info('save detection annotation file: {}'.format(dst_name))
    return dst_name

# file name do NOT have space character
def _modify_classify_annotations(
        src_name, dst_path, abs_work_path, abs_work_folders, abs_work_default_folders, all_image_folders):
    """
    修改分类标注文件，将相对路径转换为绝对路径。
    
    Args:
        src_name (str): 源文件名，包括路径。
        dst_path (str): 目标保存路径。
        abs_work_path (str): 工作空间的绝对路径。
        abs_work_folders (list[str]): 工作空间的所有子目录文件名。
        abs_work_default_folders (list[str]): 工作空间的默认子目录文件名。
        all_image_folders (set[str]): 工作空间下的所有图片文件夹
    
    Returns:
        str, optional: 返回目标文件名，如果转换失败则返回None。
    
    Raises:
        None.
    """
    with open(src_name) as f:
        lines = f.readlines()
        
        dst_name = os.path.join(dst_path, src_name.split('/')[-1])
        with open(dst_name, 'w') as dst_f:
            for l in lines:
                frags = l.strip().split(NX_SPLIT_CHAR)
                frags[0] = _cvt_2_abs_path(
                        frags[0], abs_work_path, 'images', abs_work_folders, abs_work_default_folders)
                dst_f.write(NX_SPLIT_CHAR.join(frags) + '\n')
                all_image_folders.add(os.path.dirname(frags[0]))
    
            bcelogger.info('save classify annotation file: {}'.format(dst_name))
            return dst_name
    return None

# file name do NOT have space character
def _modify_segment_annotations(src_name, dst_path, abs_work_path):
    """
    修改分割注释，将相对路径转换为绝对路径。
    
    Args:
        src_name (str): 源文件名，包括路径。
        dst_path (str): 目标路径。
        abs_work_path (str): 工作路径。
    
    Returns:
        str, optional: 返回新的文件名，如果修改失败则返回None。
    
    Raises:
        None.
    """
    with open(src_name) as f:
        lines = f.readlines()
        
        dst_name = os.path.join(dst_path, src_name.split('/')[-1])
        with open(dst_name, 'w') as dst_f:
            for l in lines:
                frags = l.split(NX_SPLIT_CHAR)
                frags[0] = _cvt_2_abs_path(frags[0], abs_work_path) # image
                frags[1] = _cvt_2_abs_path(frags[1], abs_work_path) # mask
                dst_f.write(NX_SPLIT_CHAR.join(frags) + '\n')
    
            bcelogger.info('save segment annotation file: {}'.format(dst_name))
            return dst_name
    return None
            
def _copy_annotation_file_2_backup_path(name, backup_path):
    """
    将指定名称的注释文件复制到备份路径中。
    
    Args:
        name (str): 需要被复制的注释文件名称，包括完整路径。
        backup_path (str): 备份路径，该路径下会存在一个与原始注释文件同名的副本。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    backup_name = os.path.join(backup_path, name.split('/')[-1])
    shutil.copyfile(src=name, dst=backup_name)
    bcelogger.info('save annotation file to backup path: {}'.format(backup_name))

def _get_txt_annotation_type(name):
    """
    获取文本注释类型，如果最后一行是数字或负数加数字，则返回cls类型，否则返回seg类型。
    
    Args:
        name (str): 文件名，包含路径。
    
    Returns:
        str, optional: 返回以下三种类型之一：NX_ANNOTATION_TYPE_CLS、NX_ANNOTATION_TYPE_SEG、None。默认为None。
            - NX_ANNOTATION_TYPE_CLS (str)：cls类型，表示文本注释类型为分类。
            - NX_ANNOTATION_TYPE_SEG (str)：seg类型，表示文本注释类型为段落。
            - None (None)：如果无法确定文本注释类型，则返回None。
    """
    with open(name) as f:
        last_val = f.readlines()[0].strip().split(NX_SPLIT_CHAR)[-1]
        if last_val.isdigit() or (last_val.startswith('-') and last_val[1: ].isdigit()):
            return NX_ANNOTATION_TYPE_CLS
        else:
            return NX_ANNOTATION_TYPE_SEG # modify latter
    return None

def _get_file_annotation_type(name):
    """
    获取文件的标注类型，支持JSON和TXT两种格式。
    
    Args:
        name (str): 文件名，包含路径信息。
            JSON格式的文件应以"json"结尾，TXT格式的文件应以"txt"结尾。
    
    Returns:
        int: 返回一个整数，分别表示标注类型如下：
            0 - NX_ANNOTATION_TYPE_DET（目标检测）；
            1 - NX_ANNOTATION_TYPE_SEG（实例分割）；
            2 - NX_ANNOTATION_TYPE_ASR（语音识别）；
            3 - NX_ANNOTATION_TYPE_OCR（光学字符识别）。
    
        Raises:
            ValueError: 当文件名不是JSON或TXT格式时，会引发此错误。
    """
    if name.split('/')[-1].endswith('json'):
        return NX_ANNOTATION_TYPE_DET
    elif name.split('/')[-1].endswith('txt'):
        return _get_txt_annotation_type(name)
    else:
        raise ValueError("do NOT support annotation {}".format(name))
    
def _guess_algorith_annotation_type(annotation_path):
    """
    根据注释路径猜测算法注释类型，如果是文件则返回文件注释类型，否则返回None。
    如果注释路径为文件且存在于'train'或'val'目录下，则返回第一个找到的文件注释类型。
    
    Args:
        annotation_path (str): 注释路径，可以是文件或者目录。
    
    Returns:
        str, None: 如果注释路径是文件，返回文件注释类型；如果注释路径是目录，返回None。
    
    Raises:
        ValueError: 当注释路径不支持时，会引发ValueError异常。
    """
    if os.path.isfile(annotation_path):
        # file
        return _get_file_annotation_type(annotation_path)
    else:
        # folder
        for p in ['train', 'val']:
            names = _retrive_path(annotation_path, ['json', 'txt'], p)
            if len(names) > 0:
                return _get_file_annotation_type(names[0])
    raise ValueError("do NOT support annotation {}".format(annotation_path)) 

def _modify_annotation(src_name, dst_path, abs_work_path, all_image_folders):
    """
    根据源文件名修改对应的标注信息，返回修改后的标注文件路径或None。
    
    Args:
        src_name (str): 源文件名，包括扩展名。
        dst_path (str): 目标标注文件保存路径，不包括扩展名。
        abs_work_path (str): 绝对工作路径，用于生成新的标注文件名。
        all_image_folders (set[str]): 所有参与训练的图像文件夹集合
    
    Returns:
        str or None: 如果修改成功，返回修改后的标注文件路径；否则返回None。
    """

    # 通过提前 os.listdir() 预先缓存所有文件夹，避免后续的 os.listdir() 耗时
    bcelogger.info(f"预先 os.listdir() 以加速数据集准备部分时间")
    default_prefix = 'images'
    abs_work_folders = os.listdir(abs_work_path) if os.path.exists(abs_work_path) else []
    abs_work_default_path = os.path.join(abs_work_path, default_prefix)
    abs_work_default_folders = (
            os.listdir(abs_work_default_path) if os.path.exists(abs_work_default_path) else [])
    
    annotation_type = _guess_algorith_annotation_type(src_name)
    if annotation_type == NX_ANNOTATION_TYPE_DET:
        return _modify_detection_annotations(
                src_name, dst_path, abs_work_path, abs_work_folders, abs_work_default_folders, all_image_folders)
    elif annotation_type == NX_ANNOTATION_TYPE_CLS:
        return _modify_classify_annotations(
                src_name, dst_path, abs_work_path, abs_work_folders, abs_work_default_folders, all_image_folders)
    elif annotation_type == NX_ANNOTATION_TYPE_SEG:
        return _modify_segment_annotations(src_name, dst_path, abs_work_path)
    else:
        return None

def pre_listdir_folders(all_image_folders):
    """通过 os.listdir() 预先缓存所有文件夹，避免后续的 os.listdir() 耗时
    
    Args:
        all_image_folders (set[str]): 所有参与训练的图像文件夹集合
    """
    done_folders = set()
    for image_folder_path in all_image_folders:
        current_path = '/'
        for item in image_folder_path.split('/'):
            current_path = os.path.join(current_path, item)
            if current_path not in done_folders:
                
                try:
                    os.listdir(current_path)
                except Exception as e:
                    bcelogger.info(f"Exception occurred while listing directory: {e}")
                
                done_folders.add(current_path)
                bcelogger.info(f"warm up folder: {current_path}")
            # else pass

def std_algorithm_train(args):
    """
    Train component for ppyoloe_plus model.
    """
    windmill_client = WindmillClient(ak=args.windmill_ak,
                                     sk=args.windmill_sk,
                                     endpoint=args.windmill_endpoint)
    tracker_client = ExperimentTracker(windmill_client=windmill_client,
                                       tracking_uri=args.tracking_uri,
                                       experiment_name=args.experiment_name,
                                       experiment_kind=args.experiment_kind,
                                       project_name=args.project_name)
    setup_logger(config=dict(file_name=os.path.join(args.output_uri, "worker.log")))
    
    response = windmill_client.get_artifact(name=args.train_dataset_name)
    filesystem = windmill_client.suggest_first_filesystem(workspace_id=response.workspaceID,
                                                                       guest_name=response.parentName)
    bcelogger.info(f"------filesystem------ : {filesystem}")
    
    train_val_annotation_files = {}
    local_dst_path = '/root/annotations'
    if not os.path.exists(local_dst_path):
        os.makedirs(local_dst_path)
    
    # 获取目前全部参与训练图片所在文件夹的路径
    all_image_folders = set()
    for _path in response.metadata["paths"]:
        relative_path = windmill_client.get_path(filesystem, _path)
        local_dataset_path = os.path.join(tracker_client.work_dir, relative_path)
        bcelogger.info(f"-----local_dataset_path----- : {local_dataset_path}")
        prefix = ['train', 'val']
        for p in prefix:
            src_names = []
            if not os.path.isfile(local_dataset_path):
                src_names = _retrive_path(local_dataset_path, ['json', 'txt'], p)
            else:
                src_names.append(local_dataset_path)
            if len(src_names) <= 0:
                continue
            abs_work_path = find_upper_level_folder(src_names[0], 2) # according to document MUST have annotation-folder
            for src_name in src_names:
                dst_name = _modify_annotation(src_name, local_dst_path, abs_work_path, all_image_folders)
                if p in train_val_annotation_files:
                    train_val_annotation_files[p].append(dst_name)
                else:
                    train_val_annotation_files[p] = [dst_name]

    # 通过 os.listdir() 预先缓存所有文件夹，避免后续的 os.listdir() 耗时
    pre_listdir_folders(all_image_folders)

    # 读取 v2x config YAML 文件
    input_config_file = "/root/train_code/v2x_model_standardization/configs/input_config.yaml"
    bcelogger.info(f"------input_config_file------: {input_config_file}")

    with open(input_config_file, 'r') as f:
        config = yaml.safe_load(f)

    # 将 dataset 配置清空，读取实际的 dataset 配置，并填充
    if 'data_load' in config and isinstance(config['data_load'], dict):
        config['data_load']['train'] = {}
        config['data_load']['eval'] = {}
        config['data_load']['infer'] = {}

    task_name = config['task_name']
    bcelogger.info(f"------task_name is------: {task_name}")

    image_dir_name = "image_dir"
    data_dir_name = "dataset_dir"
    anno_dir_name = "anno_path"
    key_sample_prob = 'sample_prob'

    config['data_load']['train'][image_dir_name] = "./"
    config['data_load']['train'][data_dir_name] = '/'
    config['data_load']['train'][anno_dir_name] = train_val_annotation_files['train']
    config['data_load']['train'][key_sample_prob] = 1

    config['data_load']['eval'][image_dir_name] = "./"
    config['data_load']['eval'][data_dir_name] = '/'
    config['data_load']['eval'][anno_dir_name] = train_val_annotation_files['val']
    config['data_load']['eval'][key_sample_prob] = 1

    config['data_load']['infer'][image_dir_name] = "none"
    config['data_load']['infer'][data_dir_name] = "none"
    config['data_load']['infer'][anno_dir_name] = "none"

    if not os.path.exists(args.output_model_uri):
        os.makedirs(args.output_model_uri, exist_ok=True)

    config['output_root_dir'] = args.output_model_uri
    with open(input_config_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

    bcelogger.info(f"-----input_config_file------:{config}")

    for k, v in train_val_annotation_files.items():
        for name in v:
            _copy_annotation_file_2_backup_path(name, args.output_uri)

    trainer = Trainer(framework="PaddlePaddle", tracker_client=tracker_client)
    metric_names = [LOSS_METRIC_NAME, MAP_METRIC_NAME, AP50_METRIC_NAME, AR_METRIC_NAME]
    trainer.track_model_score(metric_names=metric_names)
    std_alg_log_name = os.path.join(args.output_uri, 'std-algorithm-train.log') 

    train_command = (
                f'cd /root/train_code/ && '
                f'package_path=$(python3 -c "import site; print(site.getsitepackages()[0])") && '
                f'python -m v2x_model_standardization ; '
                f'cd /root/{task_name} &&'
                f'bash train.sh 2>&1 | tee -a std_alg_log_name && '
                f'bash export.sh'
                )
    result = os.system(train_command)
    bcelogger.info(f"train result: {result}")
    trainer.training_exit_flag = True

    bcelogger.info('standardization-algorithm-train-log file: {}'.format(std_alg_log_name))

    # 获取模型输出，如果没有则推出
    # 6. 创建模型
    bcelogger.info(f"------begin to create model------")
    metric_name = BOUNDING_BOX_MEAN_AVERAGE_PRECISION_METRIC_NAME
    if os.path.exists(os.path.join(args.output_model_uri, "metric.json")):
        current_score = get_score_from_file(filepath=os.path.join(args.output_model_uri, "metric.json"),
                                        metric_name=metric_name)
    else:
        current_score = 1.0

    best_score, version = Model(windmill_client=windmill_client). \
        get_best_model_score(model_name=args.model_name, metric_name=metric_name)
    tags = {metric_name: str(current_score)}
    alias = None
    if current_score >= best_score and version is not None:
        alias = ["best"]
        bcelogger.info(
            f"{metric_name.capitalize()} current score {current_score} >= {best_score}, update [best]")
        tags.update(
            {"bestReason": f"current.score({current_score}) greater than {version}.score({best_score})"})
    if version is None:
        alias = ["best"]
        bcelogger.info(f"First alias [best] score: {current_score}")
        tags.update({"bestReason": f"current.score({current_score})"})

    model_name = parse_model_name(args.model_name)
    workspace_id = model_name.workspace_id
    model_store_name = model_name.model_store_name
    local_name = model_name.local_name
    response = windmill_client.create_model(workspace_id=workspace_id,
                                            model_store_name=model_store_name,
                                            local_name=local_name,
                                            display_name=args.model_display_name,
                                            category="Image/ObjectDetection",
                                            model_formats=["PaddlePaddle"],
                                            artifact_alias=alias,
                                            artifact_tags=tags,
                                            artifact_metadata={},
                                            artifact_uri=args.output_model_uri)
    bcelogger.info(f"Model {args.model_name} created response: {response}")

    # 7. 输出文件
    write_file(obj=json.loads(response.raw_data), output_dir=args.output_model_uri)


if __name__ == "__main__":
    args = parse_args()
    std_algorithm_train(args=args)
