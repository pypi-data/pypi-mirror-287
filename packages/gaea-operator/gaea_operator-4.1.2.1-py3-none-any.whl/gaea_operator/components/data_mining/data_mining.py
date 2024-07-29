#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/05
# @Author  : lidai@baidu.com
# @File    : data_mining.py
"""
import asyncio
import functools
import io
import json
import os
import random
import re
import string
import time
import typing as tp
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import bcelogger
import requests
from windmillcomputev1.client.compute_api_filesystem import parse_filesystem_name
from windmilltrainingv1.client.training_api_dataset import parse_dataset_name
import pycocotools.mask as mask_utils
import cv2
from windmillclient.client.windmill_client import WindmillClient
from bcelogger.base_logger import setup_logger
from gaea_operator.utils.videoio import Dedup, decode, process_operator

T = tp.TypeVar('T', covariant=True)

DATA_MINING_RESULT_IMAGES_DIR = "images"
DATA_MINING_RESULT_ANNOTATION_DIR = "annotations"
DATA_MINING_DIR = "data_mining"
ANNOTATION_TYPE_COCO = "COCO"
ANNOTATION_TYPE_IMAGENET = "ImageNet"
ANNOTATION_TYPE_CITYSCPAES = "Cityscapes"
INFERENCE_URL = "localhost"
INFERENCE_GRPC_PORT = "8661"
INFERENCE_HTTP_PORT = "8662"
INFERENCE_METRICS_PORT = "8912"
TRITON_LOG_FILE = "triton.log"


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK"))
    parser.add_argument("--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK"))
    parser.add_argument("--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT"))
    parser.add_argument("--project-name", type=str, default=os.environ.get("PROJECT_NAME"))
    parser.add_argument("--workspace-id", type=str, default=os.environ.get("WORKSPACE_ID"))

    parser.add_argument("--output-uri", type=str, default=os.environ.get("PF_OUTPUT_ARTIFACT_OUTPUT_URI"))
    parser.add_argument("--output-model-uri", type=str, default=os.environ.get("PF_OUTPUT_ARTIFACT_OUTPUT_MODEL_URI"))

    parser.add_argument("--work-dir", type=str, default=os.environ.get("PF_WORK_DIR"))
    parser.add_argument("--extra-work-dir", type=str, default=os.environ.get("PF_EXTRA_WORK_DIR"))

    parser.add_argument("--model-name", type=str, default=os.environ.get("MODEL_NAME"))
    parser.add_argument("--model-artifact-version", type=str, default=os.environ.get("MODEL_ARTIFACT_VERSION"))

    parser.add_argument("--input-dataset-name", type=str, default=os.environ.get("INPUT_DATASET_NAME"))
    parser.add_argument("--output-dataset-name", type=str, default=os.environ.get("OUTPUT_DATASET_NAME"))
    parser.add_argument("--label-confidence-threshold", type=str, default=os.environ.get("LABEL_CONFIDENCE_THRESHOLD"))
    parser.add_argument("--annotation-type", type=str, default=os.environ.get("ANNOTATION_TYPE"))
    parser.add_argument("--mining-keyword", type=str, default=os.environ.get("MINING_KEY_WORD"))
    parser.add_argument("--mining-keyword-description", type=str, default=os.environ.get("MINING_KEY_WORD_DESCRIPTION"))
    parser.add_argument("--mining-algorithm", type=str, default=os.environ.get("MINING_ALGORITHM"))

    parser.add_argument("--icafe-id", type=str, default=os.environ.get("ICAFE_ID"))
    parser.add_argument("--icafe-operator", type=str, default=os.environ.get("ICAFE_OPERATOR"))

    args, _ = parser.parse_known_args()

    return args


def data_mining(args):
    """
    Package component for ppyoloe_plus model.
    """

    if args.icafe_id:
        from gaea_operator.components.icafe import icafe
        icafe.sync_icafe_model_annotation_begin(args)

    windmill_client = WindmillClient(ak=args.windmill_ak,
                                     sk=args.windmill_sk,
                                     endpoint=args.windmill_endpoint)
    setup_logger(config=dict(file_name=os.path.join(args.output_uri, "worker.log")))

    # get input dataset
    work_dirs = [args.extra_work_dir, args.work_dir]
    trimmed_str = args.input_dataset_name.strip('[]')
    dataset_list = trimmed_str.split()

    # get dataset filesystem
    input_artifact_response = windmill_client.get_artifact(name=dataset_list[0])
    dataset_name = input_artifact_response.objectName
    filesystem = windmill_client.suggest_first_filesystem(workspace_id=input_artifact_response.workspaceID,
                                                          guest_name=dataset_name)

    # find dataset mining files
    dataset_mining_files_dict = _get_dataset_files(windmill_client, dataset_list, work_dirs, filesystem)

    # download ensemble model 
    model_uri = "/home/windmill/tmp/model"
    ensemble_artifact_name = args.model_name + "/versions/" + args.model_artifact_version
    bcelogger.info("downloading ensemble model: ".format(ensemble_artifact_name))
    windmill_client.dump_models(artifact_name=ensemble_artifact_name,
                                location_style="Triton", output_uri=model_uri, rename="ensemble")

    # deploy triton server
    command_template = (
        "export LD_PRELOAD=/opt/tritonserver/lib/libmmdeploy_tensorrt_ops.so && "
        "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/compat/lib:/usr/local/nvidia/lib:/usr/local"
        "/nvidia/lib64:/opt/tritonserver/lib:$LD_LIBRARY_PATH &&"
        "export PYTHONPATH= && "
        "/opt/tritonserver/bin/tritonserver --model-repository={model_uri} "
        "--pinned-memory-pool-byte-size 1073741824 --log-verbose=0 "
        "--http-port {http_port} --grpc-port {grpc_port} "
        "--metrics-port {metrics_port} --allow-auth false 2>&1 | tee -a {log_file} &"
    )
    command = command_template.format(
        model_uri=model_uri,
        http_port=INFERENCE_HTTP_PORT,
        grpc_port=INFERENCE_GRPC_PORT,
        metrics_port=INFERENCE_METRICS_PORT,
        log_file=TRITON_LOG_FILE
    )
    bcelogger.info("Triton server exec command: {}".format(command))
    exec_command = os.system(command)

    def is_triton_server_ready(inference_url, inference_http_port, check_interval=3):
        triton_ready_check_uri = f"http://{inference_url}:{inference_http_port}/v2/health/ready"
        while True:
            time.sleep(check_interval)
            try:
                response = requests.get(
                    triton_ready_check_uri, timeout=60
                )
                if response.status_code == 200:
                    bcelogger.info("Triton server ready!")
                    return True

            except requests.exceptions.RequestException as _e:
                bcelogger.error("Triton Server Not ready! Exception: %s", {_e})
            except Exception as e:
                bcelogger.error("An unexpected error occurred: %s", e)

    is_triton_server_ready(INFERENCE_URL, INFERENCE_HTTP_PORT)

    async def process(dataset_path, prediction_storage_path, mining_keyword, mining_keyword_description,
                      mining_algorithm):
        queues: list[asyncio.Queue] = []
        tasks: list[tp.Awaitable] = []
        add_queue = lambda: queues.append(asyncio.Queue(maxsize=4))

        data_dir = Path(dataset_path)

        # for debug: tasks.append(decode(data_dir.glob('**/*'), queues[-1], fps=10, inp_args={"to": 50},
        # on_error="ignore"))
        add_queue()
        tasks.append(decode(data_dir.glob('**/*'), queues[-1], fps=10, on_error="ignore"))

        add_queue()
        tasks.append(process_operator(Dedup(), async_queue=True)(queues[-2], queues[-1]))

        add_queue()
        tasks.append(do_infer(queues[-2], queues[-1],
                              mining_keyword=mining_keyword,
                              mining_keyword_description=mining_keyword_description,
                              mining_algorithm=mining_algorithm))

        if args.label_confidence_threshold:
            filter_expression = transform_rule(args.label_confidence_threshold)
            expr: str = filter_expression
            add_queue()
            tasks.append(do_filter(queues[-2], queues[-1], expr=expr))

        if not os.path.exists(prediction_storage_path):
            os.makedirs(prediction_storage_path)
        save_dir = Path(prediction_storage_path)
        add_queue()
        tasks.append(process_operator(
            functools.partial(do_save, save_dir=save_dir),
            async_queue=True,
        )(queues[-2], queues[-1]))

        results = []

        async def sink(queue):
            while True:
                item = await queue.get()
                item_result = {
                    'image_id': item.result['image_id'],
                    'file_name': str(item.meta['save_path']),
                    'shape': [item.meta['width'], item.meta['height']],
                    'predictions': item.result['predictions']
                }
                if args.annotation_type == ANNOTATION_TYPE_CITYSCPAES:
                    item_result['mask_name'] = str(item.meta['mask_name'].replace(args.work_dir, ""))
                results.append(item_result)
                queue.task_done()

        tasks.append(sink(queues[-1]))
        tasks = list(map(asyncio.create_task, tasks))
        _, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for q in queues: await q.join()
        for t in tasks: t.cancel()

        return results

    # get output dataset storage path
    output_dataset_artifact_uri_path = os.path.join(args.work_dir, DATA_MINING_DIR, _get_job_name(args.output_uri))

    # infer the input dataset list
    predictions = []
    for dataset_name, path in dataset_mining_files_dict.items():
        dataset_name_instance = parse_dataset_name(dataset_name)
        storage_path = os.path.join(output_dataset_artifact_uri_path, dataset_name_instance.local_name)
        # model inference
        prediction_result = asyncio.run(process(path, storage_path, args.mining_keyword,
                                                args.mining_keyword_description, args.mining_algorithm))
        # get inference result
        predictions.extend(prediction_result)

    annotation_path = os.path.join(output_dataset_artifact_uri_path, "annotations/")
    if args.annotation_type == ANNOTATION_TYPE_COCO:
        annotation_list = prediction_to_coco_annotation(predictions, filesystem)
        write_coco_annotation(annotation_path, annotation_list, "train.json")
        write_coco_annotation(annotation_path, annotation_list, "val.json")
    elif args.annotation_type == ANNOTATION_TYPE_IMAGENET:
        annotation_list, label_list = prediction_to_imagenet_annotation(predictions, filesystem)
        write_imagenet_annotation(annotation_path, annotation_list, label_list)
    elif args.annotation_type == ANNOTATION_TYPE_CITYSCPAES:
        annotation_list, label_list = prediction_to_cityscapes_annotation(predictions, filesystem)
        write_cityscapes_annotation(annotation_path, annotation_list, label_list)

    # create new dataset based on exist dataset
    input_artifact_response = windmill_client.get_artifact(name=dataset_list[0])
    dataset_name = input_artifact_response.objectName
    _dataset_instance = parse_dataset_name(dataset_name)
    get_output_dataset_response = windmill_client.get_dataset(workspace_id=_dataset_instance.workspace_id,
                                                              project_name=_dataset_instance.project_name,
                                                              local_name=_dataset_instance.local_name)
    dataset_category = get_output_dataset_response.category['category']

    s3_uri_path = output_dataset_artifact_uri_path.replace(args.work_dir, "s3://" + filesystem["endpoint"]) + "/"
    create_new_dataset_response = windmill_client.create_dataset(
        workspace_id=_dataset_instance.workspace_id,
        project_name=_dataset_instance.project_name,
        category=dataset_category,
        local_name=_generate_dataset_name(),
        display_name=args.output_dataset_name,
        artifact_uri=s3_uri_path,
    )
    bcelogger.info("create_dataset response: {}".format(create_new_dataset_response))
    if args.icafe_id:
        from gaea_operator.components.icafe import icafe
        icafe.sync_icafe_model_annotation_end(args)


def chunks(iterable: tp.Iterable[T], batch_size: int) -> tp.Iterator[tp.Sequence[T]]:
    """
    将一个迭代器分割成更小的批次，每个批次包含batch_size个元素。
    
    Args:
        iterable (Iterable[T]): 要被分割的迭代器。
        batch_size (int): 每个批次中元素的数量。
    
    Returns:
        Iterator[Sequence[T]]: 返回一个生成器，每个生成器是一个包含batch_size个元素的列表。如果最后一个批次不足batch_size个元素，则会丢弃多出来的元素。
    """
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


async def do_infer(
        inp_queue: asyncio.Queue['IMData'], out_queue: asyncio.Queue['IMData'],
        /,
        url: str = INFERENCE_URL + ':' + INFERENCE_HTTP_PORT, model_name: str = 'ensemble',
        mining_keyword: str = "",
        mining_keyword_description: str = "",
        mining_algorithm: str = "",
        **kwds):
    """
    异步执行模型推理。
    
    Args:
        inp_queue (asyncio.Queue['IMData']): 输入队列，包含需要推理的图像数据。
        out_queue (asyncio.Queue['IMData']): 输出队列，将推理结果写入到这里。
        url (str, optional): 服务器地址，默认为 ``'http://localhost'``。
        model_name (str, optional): 模型名称，默认为 ``'ensemble'``。
        mining_keyword( str ): 多模态模型挖掘关键词
        mining_keyword_description ( str )：多模态模型挖掘关键词描述
        mining_algorithm ( str )：多模态模型挖掘算法
        **kwds (dict, optional): 其他参数将会传递给 `AsyncioModelClient` 实例化函数。
    
    Returns:
        None, 无返回值。
    
    Raises:
        None, 没有异常抛出。
    """
    import PIL.Image as Image
    import numpy as nt

    from pytriton.client import AsyncioModelClient

    meta: dict[str, tp.Any] = {
        "block_offset_height": 0,
        "block_offset_width": 0,
        "block_scale_height": 1.0,
        "block_scale_width": 1.0,
        "score_thresh": 0.2,
        "whole_scale_height": 1.0,
        "whole_scale_width": 1.0,
        "keyword": mining_keyword,
        "description": mining_keyword_description,
        "algorithm": mining_algorithm
    }

    async with AsyncioModelClient(url, model_name, **kwds) as client:
        async def process(image: 'IMData'):
            meta["image_id"] = image.hash
            bcelogger.info(f"======do_infer meta===={meta}")
            stream = io.BytesIO()
            Image.fromarray(image.data).save(stream, format="JPEG")
            compressed: bytes = stream.getvalue()
            results: tp.Mapping[str, nt.ndarray] = await client.infer_sample(
                nt.frombuffer(compressed, dtype=nt.uint8),
                nt.frombuffer(json.dumps(meta).encode(), dtype=nt.uint8),
            )

            result: tp.Sequence[tp.Mapping[str, tp.Any]] = \
                json.loads(next(iter(results.values())).tobytes().decode())[0]

            bcelogger.info(f"======do_infer result====={result}")
            yield image.copy(compressed=compressed, result=result)

        try:
            await process_operator(process)(inp_queue, out_queue)
        finally:
            await client.close()


def do_filter(
        inp_queue: asyncio.Queue['IMData'], out_queue: asyncio.Queue['IMData'],
        /,
        expr: str,
        **kwds):
    """
    过滤输入队列中的数据，并将符合条件的数据放入输出队列中。
    
    Args:
        inp_queue (asyncio.Queue['IMData']): 待处理的数据队列，类型为 asyncio.Queue['IMData']。
        out_queue (asyncio.Queue['IMData']): 存放处理后结果的队列，类型为 asyncio.Queue['IMData']。
        expr (str, optional): 用于过滤数据的表达式，默认值为 "".
        **kwds (dict, optional): 其他可选参数，包括：
            - kwds.get('async_queue', False) (bool, optional): 是否使用异步队列，默认值为 False。
    
    Returns:
        None: 该函数没有返回值。
    """
    import pandas as xf
    # import polars as xf

    from gaea_operator.utils.label_process import elevate_fields, flatten_df, joint_predicate

    exprs: list[str] = [elevate_fields(expr)]

    # sql_expr: xf.Expr = xf.sql_expr(expr)

    def process(image: 'IMData'):
        results: tp.Sequence[tp.Mapping[str, tp.Any]] = [image.result]
        df: xf.DataFrame = xf.DataFrame.from_records(results)
        df = flatten_df(df)
        pred_s: xf.Series[bool] = joint_predicate(df, exprs)
        for index in pred_s.loc[pred_s].index.unique():
            yield image

    return process_operator(process, async_queue=True)(inp_queue, out_queue)


def do_save(
        image: 'IMData',
        /,
        save_dir: os.PathLike, name_by: str = '{hash}') -> tp.Generator['IMData', None, None]:
    """
    保存图像和掩码到指定目录。
    
    Args:
        image (IMData, 'IMData'): 待保存的图像对象，必须包含属性`compressed`、`meta`和`copy`。
        save_dir (os.PathLike, str): 保存路径，可以是字符串或者`os.PathLike`类型。默认为当前工作目录。
        name_by (str, optional): 文件名格式化字符串，将会被`{hash}`替换为图像的哈希值，默认为`'{hash}'`。
            `{hash}`之前的部分不能包含`.jpg`或者`.png`后缀。
    
    Returns:
        tp.Generator[IMData, None, None]: 返回一个生成器，每次产出一个新的`IMData`对象，其中`save_path`和`mask_name`已经更新为保存路径。
    
    Raises:
        ValueError: 如果`name_by`中包含`.jpg`或者`.png`后缀。
    """
    save_dir = Path(save_dir)

    suffix: str = '.jpg'
    name_by = name_by.rstrip(suffix) + suffix
    meta = dict[str, tp.Any](image.meta)
    save_path: Path = save_dir / name_by.format(**meta)
    save_path.write_bytes(image.compressed)
    if args.annotation_type == ANNOTATION_TYPE_CITYSCPAES:
        mask_suffix: str = '.png'
        mask_name_by = name_by.rstrip(suffix) + mask_suffix
        mask_save_path: Path = save_dir / mask_name_by.format(**meta)
        mask_save_path.write_bytes(image.compressed)
        yield image.copy(save_path=save_path, mask_name=str(mask_save_path))
    else:
        yield image.copy(save_path=save_path)


def get_confidence_threshold_expression(data):
    """
    获取置信度阈值表达式。
    
    Args:
        data (dict): dict，包含类别名称和对应的低置信度、高置信度，格式为{类别名称:（低置信度，高置信度)}。
    
    Returns:
        str: 返回一个字符串，表示所有类别的置信度阈值表达式，格式为："(predictions['categories']['name'] == '{类别名称}' "
             "and {低置信度} < predictions['categories']['confidence'] < {高置信度})"，其中{类别名称}、{低置信度}、{高置信度}
             是实际的数值。然后将这些表达式用" or "连接起来形成最终的表达式。
    """
    expressions = []

    for category_name, (low_confidence, high_confidence) in data.items():
        expr = (
            f'(predictions["categories"]["name"] == "{category_name}" '
            f'and {low_confidence} < predictions["categories"]["confidence"] < {high_confidence})'
        )
        expressions.append(expr)

    full_expression = ' or '.join(expressions)
    return full_expression


def find_fs_work_dir(filesystem_local_name, work_dirs):
    """
    查找指定文件系统名称在工作目录列表中的路径，如果没有找到则返回空字符串。
    
    Args:
        filesystem_local_name (str): 文件系统本地名称，例如"nfs://192.168.0.1/data"。
        work_dirs (list[str]): 工作目录列表，每个元素为一个字符串，例如["/home", "/mnt"]。
    
    Returns:
        str: 返回查找结果，如果找到则是包含文件系统本地名称的工作目录路径，否则是空字符串。
    """
    for s in work_dirs:
        if filesystem_local_name in s:
            return s

    return ""


def prediction_to_coco_annotation(prediction_list, filesystem):
    """
    # convert result to COCO Annotation
    # example
    # prediction_list = '''
    # [
    #   {
    #     "image_id": "8f3e30cf0f3870c7",
    #     "file_name": "1.jpg",
    #     "shape": [800, 600],
    #     "predictions": [
    #       {
    #         "bbox": [
    #           479.82977294921875,
    #           452.3573913574219,
    #           48.95965576171875,
    #           149.92831420898438
    #         ],
    #         "confidence": 0.72126305103302,
    #         "area": 7340.4384765625,
    #         "bbox_id": 0,
    #         "categories": [
    #           {
    #             "id": "person",
    #             "name": "äººä½",
    #             "confidence": 0.72126305103302
    #           }
    #         ]
    #       }
    #     ]
    #   }
    # ]
    """

    images_id_dict = dict()
    images_list = list()
    annotations_list = list()
    categories_list = list()

    category_id = 0
    category_dict = {}
    annotations_incr = 0
    image_id = 0
    for predict in prediction_list:
        if predict["file_name"] not in images_id_dict:
            image_id = len(images_id_dict) + 1
            images_id_dict[predict["file_name"]] = image_id
            s3_file_name = predict["file_name"].replace(args.work_dir, "s3://" + filesystem["endpoint"])
            images_list.append({
                "file_name": s3_file_name,
                "height": predict['shape'][0],
                "width": predict['shape'][1],
                "id": image_id,
            })

        annotations = predict.get("predictions")
        if annotations is None:
            bcelogger.info("annotations is empty: {}", annotations)
            continue

        for anno in annotations:
            categories = anno.get("categories")
            if categories is None:
                continue

            for category in categories:
                category_name = category.get("name")
                category_info = category_dict.get(category_name)
                if not category_info:
                    category_id += 1
                    category_dict[category_name] = {
                        'id': category_id,
                        "name": category_name,
                        "supercategory": category_name,
                    }

                annotations_incr += 1

                area = 0
                if "area" in anno:
                    area = anno['area']
                annotations_list.append({
                    'id': annotations_incr,
                    'image_id': image_id,
                    'bbox': anno['bbox'],
                    'confidence': anno['confidence'],
                    'area': area,
                    "iscrowd": 0,
                    "category_id": category_dict[category_name]["id"],
                    "segmentation": []
                })
    for category_name, category_info in category_dict.items():
        categories_list.append(category_info)

    return dict({
        "images": images_list,
        "annotations": annotations_list,
        "categories": categories_list,
    })


def write_coco_annotation(desc_predict_path, annotations_data, file_name):
    """
    """
    if not os.path.exists(desc_predict_path):
        os.makedirs(desc_predict_path)

    annotation_file = os.path.join(desc_predict_path, file_name)
    with open(annotation_file, 'w') as f:
        f.write(json.dumps(annotations_data, indent=2))

    bcelogger.info(f"write_coco_annotation success, annotation file: {annotation_file}")


def prediction_to_cityscapes_annotation(prediction_list, filesystem):
    """
       生成推理后的标注文件，Cityscapes格式, 模型预测出来的数据都是polygon，rle没有数据，数据举例如下
        prediction_list:
            [
                {
                    "image_id": "firesmoke.jpg",
                    "predictions": [
                        {
                            "bbox": [
                                58.88671732409424,
                                67.67577961127249,
                                19.335937031792135,
                                17.578124574356494
                            ],
                            "confidence": 1,
                            "segmentation": [
                                64.1601546964012,
                                67.67577961127249,
                                64.1601546964012,
                                ...
                                67.67577961127249
                            ],
                            "area": 0,
                            "ocr": {
                                "word": "",
                                "direction": ""
                            },
                            "features": [

                            ],
                            "bbox_id": 0,
                            "track_id": -1,
                            "categories": [
                                {
                                    "id": "0",
                                    "name": "\\u80cc\\u666f",
                                    "confidence": 1
                                }
                            ]
                        }
                    ]
                }
            ]
        """
    annotations_list = list()
    category_id = 0
    category_dict = {}

    for predict in prediction_list:
        """ 
            每个predict都是一张图片的所有预测数据
            """
        annotations = predict.get("predictions")
        if annotations is None:
            bcelogger.warning("prediction_to_cityscapes_annotation no predictions")
            continue

        file_name = predict.get("file_name")
        s3_file_name = predict["file_name"].replace(args.work_dir, "s3://" + filesystem["endpoint"])
        mask_name = predict.get("mask_name")

        height = predict['shape'][0]
        width = predict['shape'][1]
        image_mask = np.zeros(shape=(height, width), dtype=np.uint8)

        for anno in annotations:
            """ 
                anno是具体的预测数据
                """
            categories = anno.get("categories")
            if categories is None:
                continue

            segmentation_exist = True
            for category in categories:
                """ 
                    预测数据的标签信息，一个预测数据可能会有多个标签数据，所以这个地方要循环
                    """
                category_name = category.get("name")
                if not category_dict.get(category_name):
                    category_id += 1
                    category_dict[category_name] = category_id

                # 仅有分割模型可输出 segmentation，其他模型为空，不需要处理
                polygon = anno.get('segmentation', [])
                if len(polygon) == 0:
                    bcelogger.warning("segmentation is empty: {}".format(polygon))
                    bbox_predction = anno.get('bbox', [])
                    # from bbox to polygon
                    polygon = bbox_to_segmentation(bbox_predction)

                polygon_obj = mask_utils.frPyObjects([polygon], height, width)
                mask = mask_utils.decode(mask_utils.merge(polygon_obj))

                index = mask == 1
                image_mask[index] = category_id

        mask_path = os.path.join(args.work_dir, mask_name)
        cv2.imwrite(mask_path, image_mask)

        # find s3 prefix and append to mask_name 
        index = file_name.find(DATA_MINING_DIR)
        if index != -1:
            filesystem_s3_prefix = file_name[:index]
        s3_mask_path = filesystem_s3_prefix.rstrip('/') + mask_name

        annotations_list.append(f"{s3_file_name} {s3_mask_path}")

    label_list = list()
    for label in sorted(category_dict.items(), key=lambda x: x[1]):
        label_list.append(("{} {}" + os.linesep).format(label[0], label[1]))

    return annotations_list, label_list


def write_cityscapes_annotation(annotation_path, annotations_data, label_data):
    """
        生成cityscape标注文件
        """
    write_imagenet_annotation(annotation_path, annotations_data, label_data)


def bbox_to_segmentation(bbox):
    """
    将边界框转换为分割格式。

    参数:
    bbox (list or tuple): [x_min, y_min, width, height]

    返回:
    list: 分割的多边形格式 [x1, y1, x2, y2, x3, y3, x4, y4]
    """
    x_min, y_min, width, height = bbox
    x_max = x_min + width
    y_max = y_min + height

    # 多边形的四个角点
    segmentation = [
        x_min, y_min,  # 左上角
        x_max, y_min,  # 右上角
        x_max, y_max,  # 右下角
        x_min, y_max  # 左下角
    ]

    return segmentation


def prediction_to_imagenet_annotation(prediction_list, filesystem):
    """
        生成推理后的标注文件，ImageNet格式, 目前一张图片只能属于一种分类
        """
    annotations_list = list()
    category_id = 0
    category_dict = {}

    for predict in prediction_list:
        annotations = predict.get("predictions")
        if annotations is None:
            bcelogger.warning("prediction list empty: {}".format(annotations))
            continue

        for anno in annotations:
            categories = anno.get("categories")
            if categories is None:
                continue

            for category in categories:
                category_name = category.get("name")
                annotation_category_id = category_dict.get(category_name)
                if not annotation_category_id:
                    category_id += 1
                    category_dict[category_name] = category_id

                s3_file_name = predict.get("file_name").replace(args.work_dir, "s3://" + filesystem["endpoint"])
                annotations_list.append(f"{s3_file_name} {category_id}")

    label_list = list()
    for label in sorted(category_dict.items(), key=lambda x: x[1]):
        label_list.append(("{} {}" + os.linesep).format(label[0], label[1]))

    return annotations_list, label_list


def write_imagenet_annotation(annotation_path, annotations_data, label_data):
    """
        生成imagenet标注文件
        """
    if not os.path.exists(annotation_path):
        os.makedirs(annotation_path)
        bcelogger.info("write annotation: create annotation_path directory :{}".format(annotation_path))

    train_annotation_file = os.path.join(annotation_path, "train.txt")
    with open(train_annotation_file, "w") as file:
        for item in annotations_data:
            file.write(f'{item}' + os.linesep)

    eval_annotation_file = os.path.join(annotation_path, "val.txt")
    with open(eval_annotation_file, "w") as file:
        for item in annotations_data:
            file.write(f'{item}' + os.linesep)

    label_file = os.path.join(annotation_path, "labels.txt")
    with open(label_file, "w") as file:
        for item in label_data:
            file.write(f'{item}')


def _get_dataset_files(client, input_datasets, work_dirs, filesystem):
    """
    获取数据集文件，返回一个字典，键为输入的数据集名称，值为该数据集在本地工作目录下的路径。
    
    Args:
        client (Client): Client对象，用于调用API接口。
        input_datasets (List[str]): 需要处理的输入数据集列表，每个元素是一个字符串，代表数据集名称。
        work_dirs (List[str]): 本地工作目录列表，每个元素是一个字符串，代表工作目录的路径。
        filesystem (Dict[str, str]): 包含文件系统名称和终结点的字典，其中 "name" 是文件系统名称，"endpoint" 是终结点。
    
    Returns:
        Dict[str, str]: 返回一个字典，键为输入的数据集名称，值为该数据集在本地工作目录下的路径。如果找不到相应的数据集或工作目录，则返回空字典。
    """
    dataset_mining_files_path = dict()
    filesystem_instance = parse_filesystem_name(filesystem["name"])

    for input_dataset in input_datasets:
        # find dataset artifact path
        input_artifact_response = client.get_artifact(name=input_dataset)
        input_artifact_metadata = input_artifact_response.metadata
        dataset_name = input_artifact_response.objectName
        uri_s3 = input_artifact_metadata["paths"][0]

        # get dataset local path
        _dataset_work_dir = find_fs_work_dir(filesystem_instance.local_name, work_dirs)
        uri_without_s3 = uri_s3.replace("s3://" + filesystem['endpoint'], _dataset_work_dir)
        bcelogger.info("uri without s3: {}".format(uri_without_s3))

        dataset_mining_files_path[input_dataset] = uri_without_s3
        bcelogger.info("dataset_mining_files_path: {}".format(dataset_mining_files_path))
    return dataset_mining_files_path


def _get_job_name(path):
    """
    获取路径中的作业名称，如果没有找到则返回空字符串。
    
    Args:
        path (str): 需要解析的路径字符串。
    
    Returns:
        str: 返回路径中包含的作业名称，如果没有找到则返回空字符串。
    """
    match = re.search(r"job\w+", path)
    if match:
        return match.group()
    else:
        return ""


def _generate_dataset_name(prefix='ds-', length=8):
    """
    生成一个带有前缀和指定长度的随机字符串，默认前缀为'ds-'，长度为8。
    
    Args:
        prefix (str, optional): 字符串前缀，默认为'ds-'（数据集名称前缀）. Defaults to 'ds-'.
        length (int, optional): 字符串长度，默认为8. Defaults to 8.
    
    Returns:
        str: 返回一个带有前缀和指定长度的随机字符串。
    """
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return prefix + random_string


def transform_rule(input_rule):
    """
    将输入的规则转换为新的格式，以便在执行预测时使用。
    该函数会将 "name" 和 "confidence" 替换为 "predictions.categories.name" 和 "predictions.categories.confidence"。
    
    Args:
        input_rule (str): 待转换的规则字符串，形如 "(name >= 0.5)"。其中 "name" 和 "confidence" 需要被替换。
    
    Returns:
        str: 经过转换后的新规则字符串，形如 "(predictions.categories.name >= 0.5)"。
    """
    pattern = re.compile(r'(name|confidence)\s*([=!><]+)\s*("[^"]*"|\.\d+)')

    def replacement(match):
        var, op, val = match.groups()
        if var == 'name':
            new_var = 'predictions.categories.name'
        elif var == 'confidence':
            new_var = 'predictions.categories.confidence'
        return f'{new_var} {op} {val}'

    new_rule = pattern.sub(replacement, input_rule)
    return new_rule


if __name__ == "__main__":
    args = parse_args()
    bcelogger.info("args parameters {}".format(args))
    data_mining(args=args)
