#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/17
# @Author  : yanxiaodong
# @File    : imagenet_dataset.py
"""
import os
from typing import List, Any

import bcelogger
from windmillclient.client.windmill_client import WindmillClient

from .dataset import Dataset
from gaea_operator.utils import get_filepaths_in_archive


class PPOCRDataset(Dataset):
    """
    ImageNet Dataset
    """
    usages = [("train.txt", "annotation.txt"), ("val.txt", "annotation.txt")]

    def __init__(self,
                 windmill_client: WindmillClient,
                 work_dir: str,
                 extra_work_dir: str = None,
                 category: str = "Image/OCR"):
        super().__init__(windmill_client=windmill_client, work_dir=work_dir, extra_work_dir=extra_work_dir)

        self.image_prefix_path = ""
        self.labels = []

        if category == "Image/OCR":
            self.delimiter = "/t"
        elif category == "Image/TextDetection":
            self.delimiter = " "
        else:
            raise ValueError(f"Category {category} is not supported.")

    def _get_annotation(self, paths: List, base_uri: str, usage: str, work_dir: str):
        annotation_file_list = []
        for path in paths:
            path = os.path.join(work_dir, path)
            annotation_file_list = get_filepaths_in_archive(path, self.decompress_output_uri, usage)

        bcelogger.info(f"Annotation file list is: {annotation_file_list}")

        raw_data_list = []
        for file in annotation_file_list:
            text_data = open(file, "r").read()
            raw_data = text_data.strip("\n").split("\n")

            bcelogger.info(f"Parse annotation file {file}, image num is {len(raw_data)}")

            for idx in range(len(raw_data)):
                img_file, label = raw_data[idx].strip("\"").split(self.delimiter, 1)
                img_file = self._file_name_cvt_abs(img_file, file, base_uri, 1, work_dir)
                raw_data[idx] = img_file + self.delimiter + label

            raw_data_list.append(raw_data)

        return raw_data_list

    def _concat_annotation(self, raw_data_list: List):
        assert len(raw_data_list) >= 1, "The number of annotation file is 0"
        raw_data_imagenet = self._ppocr_data_raw_concat(raw_data_list)

        return raw_data_imagenet

    def _ppocr_data_raw_concat(self, raw_data: List[List]):
        raw_data_imagenet = []

        for idx, data in enumerate(raw_data):
            for item in data:
                img_file, label = item.strip("\"").split(self.delimiter, 1)
                raw_data_imagenet.append(img_file + self.delimiter + str(label))

        return raw_data_imagenet

    def _write_annotation(self, output_dir: str, file_name: str, raw_data: Any):
        if raw_data is None:
            return
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w") as fp:
            for item in raw_data:
                fp.write(item + "\n")