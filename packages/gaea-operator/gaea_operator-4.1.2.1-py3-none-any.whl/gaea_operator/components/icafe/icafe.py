#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   icafe.py
@Time    :   2024/04/17 11:00:53
@Author  :   lidai@baidu.com 
@License :   (C)Copyright 2021-2024, Baidu
@Desc    :   Sync mlops data to icafe 
'''
from icafeutil.core.icafe_util import IcafeUtil
from argparse import ArgumentParser
import bcelogger


def sync_icafe(args):
    """
    将训练过程指标同步到 icafe 对应卡片中
    
    Args:
        args (argparse.Namespace): 命令行参数对象，包含以下属性：
            - stage (str): 目标stage的名称。
            - id (str): 要同步的ICafe卡片的ID。
            - status (str): 要同步的ICafe卡片的状态。
            - stage_description (str): 目标stage的描述信息。
            - operator (str): 操作员名称。
    
    Returns:
        Any: 同步操作的结果，具体类型由ICafeUtil.sync()函数的返回值类型决定。
    
    Raises:
        无
    """
    icafe_util = IcafeUtil()
    stage = get_stage_name(args["stage"])
    sync_data = {
        "stage": stage,
        "type": "object",
        "properties": {
            "status": {
                "type": "string",
                "enum": [
                    {
                        "value": get_stage_status(args["stage"]),
                        "description": args["stage_description"]
                    }
                ]
            }
        }
    }
    try:
        if not args['id'] or not args['operator']:
            bcelogger.error(f"sync_icafe no icafe info args: {args}")
            return
        ret = icafe_util.sync(card_id=args["id"], status=args["status"], data=sync_data, operator=args["operator"])
        if ret["code"] != 200:
            raise SyncError(f"Unexpected response code: {ret['code']}")

        bcelogger.info(f"sync_icafe success: ret: {ret} args: {args} sync_data:{sync_data}")
    except SyncError as e:
        bcelogger.error(f"sync_icafe error: {e} ret: {ret} args: {args} sync_data:{sync_data}")
    except Exception as e:
        bcelogger.error(f"sync_icafe error: {e} ret: {ret} args: {args} sync_data:{sync_data}")


class SyncError(Exception):
    """
      SyncError exception
      """
    pass


def get_stage_name(stage):
    """
    根据输入的 stage 名称, 返回 scheme 数据
    
    Args:
    - stage (str): 数据处理的阶段名称，格式为"stage_name.sub_stage_name"。
    
    Returns:
    - str: 数据文件夹名称，格式为"Data/StageName"。
    
    """
    stage_info = stage.split(".")
    if len(stage_info) > 0:
        if stage_info[0] == "aigc":
            return "Data/AIGC"
        if stage_info[0] == "web_spider":
            return "Data/WebSpider"
        if stage_info[0] == "manual_annotation":
            return "Data/ManualAnnotation"
        if stage_info[0] == "model_annotation":
            return "Data/ModelAnnotation"
        if stage_info[0] == "train":
            return "Data/Train"
        if stage_info[0] == "eval":
            return "Data/Eval"
        if stage_info[0] == "transform":
            return "Data/Transform"
        if stage_info[0] == "transform_eval":
            return "Data/TransformEval"
        if stage_info[0] == "package":
            return "Data/Package"
        if stage_info[0] == "inference":
            return "Data/Inference"
    return "Data/Other"


def get_stage_status(stage):
    """
    获取 stage 状态
    
    Args:
        stage (str): 包含stage信息的字符串，格式为"stage.status"。
    
    Returns:
        str: stage的状态，如果stage信息格式不正确，则返回"unknown"。
    
    """
    stage_info = stage.split(".")
    if len(stage_info) > 1:
        return stage_info[1]
    return "unknown"


def sync_icafe_train_start(args):
    """
    同步ICAFE的模型训练开始状态，并更新ICAFE的状态信息。
    
    Args:
        args (dict): 包含以下键值对：
            - icafe_id (str) - ICAFE的ID。
            - icafe_operator (str) - ICAFE的操作者。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型训练开始",
        "stage": "train.start",
        "stage_description": "模型训练开始"
    }

    sync_icafe(sync_args)


def sync_icafe_train_end(args):
    """
    同步ICAFE的模型训练结束状态，包括ID、操作员、状态、阶段和阶段描述。
    
    Args:
        args (dict): 包含以下字段：
            - icafe_id (str) - ICAFE ID。
            - icafe_operator (str) - ICAFE 操作员。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型训练结束",
        "stage": "train.end",
        "stage_description": "模型训练结束"
    }

    sync_icafe(sync_args)


def sync_icafe_eval_start(args):
    """
    同步ICAFE的模型评估开始状态，并更新ICAFE的状态信息。

    Args:
        args (dict): 包含以下键值对：
            - icafe_id (str) - ICAFE的ID。
            - icafe_operator (str) - ICAFE的操作者。

    Returns:
        None.

    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型评估开始",
        "stage": "eval.start",
        "stage_description": "模型评估开始"
    }

    sync_icafe(sync_args)


def sync_icafe_eval_end(args):
    """
    同步ICAFE的模型评估结束状态，包括ID、操作员、状态、阶段和阶段描述。

    Args:
        args (dict): 包含以下字段：
            - icafe_id (str) - ICAFE ID。
            - icafe_operator (str) - ICAFE 操作员。

    Returns:
        None.

    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型评估结束",
        "stage": "eval.end",
        "stage_description": "模型评估结束"
    }

    sync_icafe(sync_args)


def sync_icafe_transform_start(args):
    """
    同步ICAFE模型转换开始状态，将ICAFE的ID、操作员、状态更新为模型转换开始。
    
    Args:
        args (argparse.Namespace): 包含了ICAFE的ID、操作员等信息的命名空间对象。其中包含以下属性：
            - icafe_id (str): ICAFE的ID。
            - icafe_operator (str): ICAFE的操作员。
    
    Returns:
        None; 无返回值，直接进行同步操作。
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型转换开始",
        "stage": "transform.start",
        "stage_description": "模型转换开始"
    }

    sync_icafe(sync_args)


def sync_icafe_transform_end(args):
    """
    同步ICAFE模型转换结束状态，并更新对应的状态信息。
    
    Args:
        args (obj): ICAFETransformEndArgs类型的对象，包含以下属性：
            - icafe_id (str) - ICAFE任务ID。
            - icafe_operator (str) - ICAFE任务操作者。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型转换结束",
        "stage": "transform.start",
        "stage_description": "模型转换结束"
    }

    sync_icafe(sync_args)


def sync_icafe_transform_eval_start(args):
    """
    同步ICAFE模型转换评估开始状态，将ICAFE的ID、操作员、状态更新为模型转换开始。

    Args:
        args (argparse.Namespace): 包含了ICAFE的ID、操作员等信息的命名空间对象。其中包含以下属性：
            - icafe_id (str): ICAFE的ID。
            - icafe_operator (str): ICAFE的操作员。

    Returns:
        None; 无返回值，直接进行同步操作。
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型转换评估开始",
        "stage": "transform_eval.start",
        "stage_description": "模型转换评估开始"
    }

    sync_icafe(sync_args)


def sync_icafe_transform_eval_end(args):
    """
    同步ICAFE模型转换结束状态，并更新对应的状态信息。

    Args:
        args (obj): ICAFETransformEndArgs类型的对象，包含以下属性：
            - icafe_id (str) - ICAFE任务ID。
            - icafe_operator (str) - ICAFE任务操作者。

    Returns:
        None.

    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型转换评估结束",
        "stage": "transform_eval.end",
        "stage_description": "模型转换评估结束"
    }

    sync_icafe(sync_args)


def sync_icafe_package_start(args):
    """
    同步ICAFE 模型组装状态，将ICAFE ID、操作员、状态、阶段和阶段描述等信息传入sync_icafe函数中进行同步。
    
    Args:
        args (argparse.Namespace): 包含ICAFE ID、操作员等信息的命名空间对象。包括以下属性：
            - icafe_id (str): ICAFE ID。
            - icafe_operator (str): ICAFE 操作员。
    
    Returns:
        None.
        通过调用sync_icafe函数来实现同步操作。
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型包组装开始",
        "stage": "package.start",
        "stage_description": "模型包组装开始"
    }

    sync_icafe(sync_args)


def sync_icafe_package_end(args):
    """
    同步ICAFE 模型包组装结束，更新状态为模型封装结束。
    
    Args:
        args (argparse.Namespace): 命令行参数，包含以下属性：
            - icafe_id (str) - ICAFE任务ID
            - icafe_operator (str) - ICAFE操作人员名称
    
    Returns:
        None
    
    Raises:
        None
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型包组装结束",
        "stage": "package.end",
        "stage_description": "模型包组装结束"
    }

    sync_icafe(sync_args)


def sync_icafe_inference_start(args):
    """
    同步ICAFE的推理开始，将状态更新为评测开始。
    
    Args:
        args (argparse.Namespace): 命令行参数，包含以下字段：
            - icafe_id (str) - ICAFE ID。
            - icafe_operator (str) - ICAFE操作员。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型包评估开始",
        "stage": "eval.start",
        "stage_description": "模型包评估开始"
    }

    sync_icafe(sync_args)


def sync_icafe_inference_end(args):
    """
    同步ICAFE的推理结束，包括更新状态和发送日志信息。
    
    Args:
        args (dict): 字典类型，包含以下键值对：
            - icafe_id (str) - ICAFE任务ID；
            - icafe_operator (str) - ICAFE操作者名称；
            - icafe_result (dict) - ICAFE任务结果，包含以下键值对：
                - status (str) - ICAFE任务状态，例如'评测中'、'评测结束'等；
                - stage (str) - ICAFE任务阶段，例如'eval.start'、'eval.stop'等；
                - stage_description (str) - ICAFE任务阶段描述，例如'评测开始'、'评测结束'等。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "模型包评估结束",
        "stage": "eval.stop",
        "stage_description": "模型包评估结束"
    }

    sync_icafe(sync_args)


def sync_icafe_annotation_end(args):
    """
    同步ICAFE的数据标注结束状态，并更新对应的任务信息。
    
    Args:
        args (argparse.Namespace): 包含以下参数：
            - icafe_id (str) - ICAFE任务ID；
            - icafe_operator (str) - ICAFE任务操作者。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "数据标注结束",
        "stage": "manual_annotation.stop",
        "stage_description": "数据标注结束"
    }

    sync_icafe(sync_args)


def sync_icafe_model_annotation_begin(args):
    """
    同步ICAFE的模型预标注开始状态，并更新对应的任务信息。
    
    Args:
        args (argparse.Namespace): 包含以下参数：
            - icafe_id (str) - ICAFE任务ID；
            - icafe_operator (str) - ICAFE任务操作者。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "数据挖掘筛选开始",
        "stage": "model_annotation.start",
        "stage_description": "数据挖掘筛选开始"
    }

    sync_icafe(sync_args)


def sync_icafe_model_annotation_end(args):
    """
    同步ICAFE的数据标注结束状态，并更新对应的任务信息。
    
    Args:
        args (argparse.Namespace): 包含以下参数：
            - icafe_id (str) - ICAFE任务ID；
            - icafe_operator (str) - ICAFE任务操作者。
    
    Returns:
        None.
    
    Raises:
        None.
    """
    sync_args = {
        "id": args.icafe_id,
        "operator": args.icafe_operator,
        "status": "数据挖掘筛选结束",
        "stage": "model_annotation.stop",
        "stage_description": "数据挖掘筛选结束"
    }

    sync_icafe(sync_args)


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--id", type=str, default='')
    parser.add_argument("--status", type=str, default='')
    parser.add_argument("--stage", type=str, default='')
    parser.add_argument("--stage_description", type=str, default='')
    parser.add_argument("--operator", type=str, default='')

    args, _ = parser.parse_known_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    sync_args = {
        "id": args.icafe_id,
        "status": args.status,
        "stage": args.stage,
        "stage_description": args.stage_description,
        "operator": args.icafe_operator,
    }
    sync_icafe(sync_args)
