#! /usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Created on Thu Jul 23 13:45:41 2020

@author: luonairui

kill %%; clear; LD_LIBRARY_PATH=/opt/conda/envs/data/lib PYTHONPATH=/opt/conda/envs/data/lib/python311.zip:/opt/conda/envs/data/lib/python3.11:/opt/conda/envs/data/lib/python3.11/lib-dynload:/opt/conda/envs/data/lib/python3.11/site-packages:/usr/local/lib/python3.8/dist-packages ipython --pdb -i -m gaea_operator.components.annotation.annotation
"""

# from __future__ import annotations

import dataclasses, io, json, os, time, typing as tp, urllib.request
import bcelogger
import boto3
import typer

from botocore.client import Config as BotoConfig
from fnmatch import fnmatch
from multiprocessing.dummy import Pool

from gaea_operator.utils.crowdtest_api import CrowdtestApi
from gaea_operator.utils.txt2coco import txt2coco
from gaea_operator.utils.typer_helper import dataclass_cli
from gaea_operator.utils.windmill_utils import (
    CV_WORKSPACE_ID, CV_PROJECT_NAME, FS_MOUNT_PATH_PREFIX,
    artifact_paging, create_dataset, windmill_client,
)


Meta: tp.TypeAlias = tp.Mapping[str, tp.Any]

app = typer.Typer()


def to_url(host: str) -> str:
    """
    将字符串转换为URL格式。如果字符串已经是URL，则直接返回该字符串；否则，会在前面添加'http://'或'https://'，并且如果字符串以':443'结尾，则会使用'https://'。
    
    Args:
        host (str): 需要转换的字符串，可能包含端口号。
    
    Returns:
        str: 转换后的URL格式字符串，始终包含'http://'或'https://'。
    """
    if '://' in host: return host
    if host.endswith(':443'): return f'https://{host}'
    return f'http://{host}'


def get_dataset(**kwds) -> Meta:
    """
    获取指定属性的数据集，如果不存在则抛出ValueError异常。
    
    Args:
        **kwds (Dict[str, Any], optional): 键值对参数，用于过滤数据集属性，默认为空字典，表示返回所有数据集（Optional)
            - key (str): 数据集属性名称，例如"name"、"description"等（Optional)
            - value (Any): 数据集属性值，类型可以是任意类型，但必须与key中的属性值类型一致（Optional)
    
    Raises:
        ValueError: 当输入的kwds无法匹配到任何数据集时会抛出此异常
    
    Returns:
        Meta (Dict[str, Any]): 包含所有数据集属性及其值的字典，包括id、name、description等属性（Dict[str, Any])
    """
    page: int = 1
    while True:
        bcelogger.debug('listing dataset page %d ...', page)
        res: 'BceResponse' = windmill_client.list_dataset(
            CV_WORKSPACE_ID, CV_PROJECT_NAME,
            page_request=artifact_paging(page_no=page, orderby="created_at"),
        )
        if not res.result: raise ValueError(kwds)
        for item in res.result:
            if all(item[k] == v for k, v in kwds.items()): return item
        page += 1


def get_dataset_filesystem(
        dataset: Meta,
        **kwds) -> Meta:
    """
    获取数据集的文件系统信息。
    
    Args:
        dataset (Meta, required): 包含数据集元数据的字典，必须包含 "artifact" 键，该键下应包含 "workspaceID" 和 "parentName" 键。
        kwargs (dict, optional): 可选参数，用于传入其他可选参数，例如 "fsType"、"mountPath"、"readOnly" 等。默认值为 None。
    
    Returns:
        Meta (dict): 包含文件系统信息的字典，包括 "name"（文件系统名称）、"type"（文件系统类型）、"mountPath"（挂载路径）、"readOnly"（是否只读）等键值对。
    
    Raises:
        None。
    """
    return windmill_client.suggest_first_filesystem(
        dataset["artifact"]["workspaceID"], dataset["artifact"]["parentName"],
        **kwds)


def list_objects(
        s3_client: 'S3', bucket_name: str,
        prefix: str = '',
        **kwds) -> tp.Generator[Meta, None, None]:
    """
    列出指定桶中的对象，支持分页。
    
    Args:
        s3_client (S3, 'S3'): S3客户端实例。
        bucket_name (str): 桶名。
        prefix (str, optional): 前缀过滤器，默认为''.
        **kwds (dict, optional): 其他可选参数将会传递给`s3_client.list_objects_v2()`方法。
    
    Yields:
        Object Meta
    
    Raises:
        无。
    """
    while True:
        bcelogger.debug('listing objects with kwds %r ...', kwds)
        res: Meta = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix, **kwds)
        if not res["Contents"]: break
        yield from res["Contents"]
        if "NextContinuationToken" in res:
            kwds["ContinuationToken"] = res['NextContinuationToken']
        else:
            break
        # break # DEBUG:


def filter_objects(
    s3_client: 'S3', bucket_name: str,
    objects: tp.Iterable[Meta],
    mime_type: tp.Optional[str] = 'image/*', fnpattern: tp.Optional[str] = '*.*p*g',
) -> tp.Generator[Meta, None, None]:
    """
    过滤出符合条件的对象，包括MIME类型和文件名模式。
    
    Args:
        s3_client (S3, 'S3'): S3客户端实例。
        bucket_name (str): 存储桶名称。
        objects (Iterable[Meta]): 需要过滤的对象列表，元素为字典格式，包含键值对 {"Key": "key1", ...}。
        mime_type (str, optional): MIME类型，默认为'image/*'。
        fnpattern (str, optional): 文件名模式，默认为'*.*p*g'。
    
    Yields:
        Object Meta
    
    Raises:
        None
    """
    mime_type_parts: tp.Optional[list[str]] = \
        mime_type and [p for p in mime_type.split('/') if p != '*']
    for obj in objects:
        if fnpattern and not fnmatch(obj["Key"], fnpattern): continue
        if mime_type_parts:
            res: Meta = s3_client.head_object(Bucket=bucket_name, Key=obj["Key"])
            content_type: str = res.get("ContentType", '')
            mime_type_parts_: list[str] = content_type.partition(';')[0].split('/')
            if mime_type_parts != mime_type_parts_[:len(mime_type_parts)]: continue
        yield obj


def make_publish_annotation(
        s3_client: 'S3', bucket_name: str,
        prefix: str = '', expires: int = 604800,
        annotation_fields: tp.Optional[tp.Mapping[str, str]] = None,
        **kwds) -> str:
    """
    生成发布注解。将所有符合条件的对象列表转换为一个包含文件名、URL和其他指定字段的表格，并返回这个表格的字符串形式。
    
    Args:
        s3_client (S3, 'S3'): S3客户端对象。
        bucket_name (str): 存放对象的桶名称。
        prefix (str, optional, default=''): 对象键前缀。默认为空字符串。
        expires (int, optional, default=604800): URL过期时间（以秒为单位）。默认为7天。
        annotation_fields (tp.Mapping[str, str] | None, optional, default=None): 要添加到每行中的额外字段。如果未提供，则不会添加任何字段。默认为None。
        **kwds (dict, optional): 传递给filter_objects函数的关键字参数。默认为空字典。
    
    Returns:
        str: 送标数据文本
    
    Raises:
        None: 没有引发任何异常。
    """
    annotation_fields = annotation_fields or dict()
    it: tp.Iterable[Meta] = list_objects(s3_client, bucket_name, prefix=prefix)
    it = filter_objects(s3_client, bucket_name, it, **kwds)
    stream = io.StringIO()
    stream.write('frame_id\tfile_name\t') 
    for key in annotation_fields.keys(): stream.write(f'{key}\t')
    stream.write('bos_key\n')
    def make_row(args):
        idx, obj = args
        url: str = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": obj["Key"]},
            ExpiresIn=expires,
        )
        return (idx, obj["Key"][len(prefix):], url)
    with Pool(processes=64) as pool:
        for *args, url in pool.imap(make_row, enumerate(it)):
            for arg in args: stream.write(f'{arg}\t')
            for val in annotation_fields.values(): stream.write(f'{val}\t')
            stream.write(f'{url}\n')
    return stream.getvalue()


@dataclasses.dataclass
class Args(object):
    dataset_filter_json: str = json.dumps(
        dict[str, tp.Any](displayName='牡丹数据收集'))
    dataset_create_name: tp.Optional[str] = None
    annotation_filter_json: str = json.dumps(
        dict[str, tp.Any](mime_type=None, fnpattern='*.*p*g'))
    annotation_fields_json: str = json.dumps(
        dict[str, str](task_id='WholeImageTrafficlight', start_time='0'))
    annotation_categories_json: str = json.dumps([
        {"id": 1, "name": "car"}, {"id": 2, "name": "truck"},
    ])
    annotation_publish: str = 'annotation.txt'
    annotation_deliver: str = 'label.txt'
    annotation_coco: str = 'train.json'
    annotation_expires: int = 604800
    annotation_offline: bool = True
    annotation_aksk: str = 'ZNJG:ZNJG123'
    annotation_template_id: str = '43723'
    annotation_data_id: tp.Optional[str] = None


def publish(s3_uri: str, filesystem: Meta, args: Args) -> str:
    annotation_filter: tp.Mapping[str, tp.Any] = json.loads(args.annotation_filter_json)
    annotation_fields: tp.Mapping[str, str] = json.loads(args.annotation_fields_json)

    s3_client: 'S3' = boto3.client(
        "s3",
        aws_access_key_id=filesystem["credential"]["accessKey"],
        aws_secret_access_key=filesystem["credential"]["secretKey"],
        endpoint_url=to_url(filesystem["host"]),
        config=BotoConfig(signature_version='s3v4'),
    )
    bucket_name, _, s3_path = s3_uri.lstrip('s3://').partition('/')
    data: str = make_publish_annotation(
        s3_client, bucket_name,
        prefix=(s3_path + '/'), annotation_fields=annotation_fields,
        **annotation_filter)
    object_key: str = os.path.join(s3_path, args.annotation_publish)
    res: Meta = s3_client.put_object(
        Bucket=bucket_name, Key=object_key,
        Body=data.encode(),
        ContentType="text/plain",
    )
    bcelogger.info('put annotation publish to %s: %s', object_key, res)
    assert res["ResponseMetadata"]["HTTPStatusCode"] == 200, res["ResponseMetadata"]

    url: str = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": object_key},
        ExpiresIn=args.annotation_expires,
    )
    annotation_api = CrowdtestApi(args.annotation_offline, args.annotation_template_id)
    annotation_api.productline_name, annotation_api.secret = args.annotation_aksk.split(':')
    bcelogger.info('publishing annotation %s with %s ...', url, vars(annotation_api))
    data_id = str(annotation_api.data_project_fill(url)["project_data_id"])
    bcelogger.info('data_id: %s', data_id)
    return data_id


def deliver(fs_path: str, args: Args) -> Meta:
    assert args.data_id

    annotation_categories: tp.Mapping[str, tp.Any] = json.loads(args.annotation_categories_json)

    annotation_api = CrowdtestApi(args.annotation_offline, args.annotation_template_id)
    while True:
        try:
            bcelogger.info('delivering annotation %s ...', args.data_id)
            annotation_url: str = annotation_api.get_converted_file(args.data_id)["url"]
        except (Exception, ):
            bcelogger.exception('')
        else:
            bcelogger.info('annotation_url: %s', annotation_url)
            if annotation_url: break
        time.sleep(600)
    # annotation_url: str = 'http://bj.bcebos.com/crowdtest-online/upload/242503312_saugoxbk_9c5651c86d3c1a424dd3267fa8fa6ffe.txt'
    local_file: str = os.path.join(fs_path, args.annotation_deliver)
    urllib.request.urlretrieve(annotation_url, filename=local_file)
    label_data: tp.Mapping[str, tp.Any] = {
        "annotations": [], "images": [], "categories": annotation_categories,
    }
    bcelogger.info('running txt2coco: %s %s ...', fs_path, local_file)
    txt2coco(fs_path, local_file, label_data)
    json.dump(label_data, open(args.annotation_coco, "w"))
    res: tp.Any = create_dataset(fs_path, args.dataset_create_name, annotation_format="Coco")
    bcelogger.info('dataset created: %s', res)
    return res


@dataclass_cli
def main(args: Args):
    """
    主函数，负责处理命令行参数并执行相应的操作。
    
    Args:
        args (Args, optional): 命令行参数对象，默认为 Args()。可以自定义参数名和类型，但必须包含所需的参数。
    
    Returns:
        None: 该函数没有返回值。
    """
    dataset_filter: Meta = json.loads(args.dataset_filter_json)

    dataset: Meta = get_dataset(**dataset_filter)
    bcelogger.info('got dataset: %s', dataset)
    filesystem: Meta = get_dataset_filesystem(dataset)
    bcelogger.info('got filesystem: %s', filesystem)
    assert len(dataset["artifact"]["metadata"]["paths"]) == 1, dataset["artifact"]["metadata"]
    assert filesystem["kind"] == "s3", filesystem

    s3_uri: str = dataset["artifact"]["metadata"]["paths"][0]
    relative_path: str = windmill_client.get_path(filesystem, s3_uri)
    assert s3_uri.endswith(relative_path), (s3_uri, relative_path)

    fs_path_prefix: str = s3_uri[:-len(relative_path)].rstrip('/')
    fs_path: str = s3_uri.replace(fs_path_prefix, FS_MOUNT_PATH_PREFIX)
    bcelogger.info('s3_uri: %s, fs_path: %s', s3_uri, fs_path)

    if not args.data_id: args.data_id = publish(s3_uri, filesystem, args=args)
    if not args.dataset_create_name: args.dataset_create_name = f'{dataset["displayName"]}-coco'
    deliver(fs_path, args=args)


if __name__ == "__main__":
    from bcelogger.base_logger import setup_logger

    setup_logger(config=dict(file_name='worker.log'))
    typer.run(main)
