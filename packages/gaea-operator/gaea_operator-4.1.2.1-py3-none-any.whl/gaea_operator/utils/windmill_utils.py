# -*- coding: utf-8 -*-
"""
Copyright(C) 2023 baidu, Inc. All Rights Reserved

# @Time : 2024/6/6 11:20
# @Author : zhangxin92
# @Email: zhangxin92@baidu.com
# @File : windmill_utils.py
# @Software: PyCharm
"""
import os
from typing import Optional
import random
import string

from windmillclient.client.windmill_client import WindmillClient
from windmillartifactv1.client.paging import PagingRequest as artifact_paging
from windmilltrainingv1.client.training_api_dataset import DatasetName

WINDMILL_AK = 'f8ebc9660a314986bfda184867085462'
WINDMILL_SK = '5e0a23d400264789ab09ece5987477bc'
WINDMILL_ENDPOINT = 'http://10.27.240.5:8340'
CV_WORKSPACE_ID = 'cv'
CV_PROJECT_NAME = 'cvzt'
FS_MOUNT_PATH_PREFIX = '/home/paddleflow/storage/mnt/fs-root-cvfs'
IMAGE_EXTENSIONS = {'.jpg', '.JPG', '.jpeg', '.JPEG'}
ANNOTATION_FORMAT_COCO = 'COCO'
ANNOTATION_FORMAT_IMAGENET = 'ImageNet'
ANNOTATION_FORMAT_CITYSCAPES = 'Cityscapes'

windmill_client = WindmillClient(ak=WINDMILL_AK,
                                 sk=WINDMILL_SK,
                                 endpoint=WINDMILL_ENDPOINT)


def list_dataset():
    response = windmill_client.list_dataset(workspace_id=CV_WORKSPACE_ID,
                                            project_name=CV_PROJECT_NAME,
                                            tags=None,
                                            page_request=artifact_paging(page_no=1,
                                                                         page_size=500,
                                                                         orderby='created_at',
                                                                         order='desc'))

    dataset_list = []

    if response.result:
        dataset = response.result[0]
        filesystem = windmill_client.suggest_first_filesystem(workspace_id=dataset['artifact']['workspaceID'],
                                                              guest_name=dataset['artifact']['parentName'])
        origin_path = dataset['artifact']['metadata']['paths'][0]
        relative_path = windmill_client.get_path(filesystem, origin_path)
        fs_path_prefix = origin_path.replace(relative_path, "").rstrip("/")
        for dataset in response.result:
            local_name = dataset['localName']
            display_name = dataset['displayName']
            version = dataset['artifact']['version']
            origin_path = dataset['artifact']['metadata']['paths'][0]
            dataset_name = display_name + '_' + local_name + ':' + str(version)
            path = origin_path.replace(fs_path_prefix, FS_MOUNT_PATH_PREFIX)

            # 过滤调文件路径内未包含图片的数据集（只有路径内包含图片的数据集才可以进行标注）
            if not is_contains_image(path):
                continue

            dataset_list.append({
                'dataset_name': dataset_name,
                'path': path
            })

    return dataset_list


def is_contains_image(path, depth=2):
    # 内部函数：递归遍历目录并检查深度
    def search_images(current_path, current_depth):
        if not os.path.isfile(current_path) and not os.path.isdir(current_path):
            return False
        # 检查当前深度是否超过最大深度
        if current_depth > depth:
            return False

        # 遍历当前目录下的所有文件和子目录
        for entry in os.listdir(current_path):
            entry_path = os.path.join(current_path, entry)
            if os.path.isfile(entry_path):
                # 检查文件的扩展名
                if any(entry_path.endswith(ext) for ext in IMAGE_EXTENSIONS):
                    return True
            elif os.path.isdir(entry_path):
                # 递归检查子目录
                if search_images(entry_path, current_depth + 1):
                    return True
        return False

    # 开始搜索
    return search_images(path, 1)


def create_dataset(
        dir_path: str,
        display_name: str,
        annotation_format: Optional[str] = "Coco",
):
    """
    创建数据集
    Args:
        dir_path (str): 当前标注项目所选的包含图片的文件夹的路径
        display_name (str): 数据集中文名
        annotation_format (str): 数据集标注格式: 当前仅支持Coco
    Returns:
            dict: The response from the server.
    """
    # 数据集名字
    local_name = "ds-" + random_string()
    # 数据集类别（当前仅支持图像检测）
    category = "Image/ObjectDetection"
    # 数据集描述
    description = display_name + "（人工标注组件导出数据集）"
    # 数据集格式
    annotation_format = annotation_format.lower()
    if annotation_format == 'coco':
        annotation_format = ANNOTATION_FORMAT_COCO
    elif annotation_format == 'cityscapes':
        annotation_format = ANNOTATION_FORMAT_CITYSCAPES
    elif annotation_format == 'imagenet':
        annotation_format = ANNOTATION_FORMAT_IMAGENET
    # 数据集版本保存路径
    dataset_name = DatasetName(workspace_id=CV_WORKSPACE_ID,
                               project_name=CV_PROJECT_NAME,
                               local_name=local_name)
    object_name = dataset_name.get_name()
    location_resp = windmill_client.create_location(object_name=object_name)
    artifact_uri = location_resp.location
    # 数据集路径
    fs_path_prefix = artifact_uri.replace(object_name, " ").split(" ")[0].rstrip("/")
    dataset_path = dir_path.replace(FS_MOUNT_PATH_PREFIX, fs_path_prefix)

    # 创建数据集
    dataset_resp = windmill_client.create_dataset(workspace_id=CV_WORKSPACE_ID,
                                                  project_name=CV_PROJECT_NAME,
                                                  local_name=local_name,
                                                  category=category,
                                                  description=description,
                                                  display_name=display_name,
                                                  data_type='Image',
                                                  annotation_format=annotation_format,
                                                  artifact_uri=artifact_uri,
                                                  artifact_alias=[],
                                                  artifact_tags={},
                                                  artifact_metadata={'paths': [dataset_path]})

    # print(dataset_resp)


def random_string():
    """随机生成8位字符串
    :return: string key value
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(8)]
    random_letters_and_digits = ''.join(str_list)
    return random_letters_and_digits


if __name__ == "__main__":
    list_dataset()
    # create_dataset("/home/paddleflow/storage/mnt/fs-root-cvfs/dataset/net_search/test_crawler_pipline_0528",
    #                "测试创建数据集接口2")
