#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : det_box.py
"""
#coding=utf-8
import os
import json
from re import A
from unittest import result
import numpy as np
import yaml
import logging

import sys
import numpy as np
#--coding:utf-8--

class DetBox:
    """
    DetBox is a class that represents a detection box.
    """
    type_id_ = ''
    score_ = 0.0
    xmin_ = 0
    ymin_ = 0
    xmax_ = 0
    ymax_ = 0
    type_name_ = ''
    super_id_ = ''
    """
    检测框类，包含检测框的属性
    """
    def __init__(self, xmin, ymin, xmax, ymax, args):
        """
            Initialize the object with the given parameters.
        
        Args:
            xmin (int): The x-coordinate of the top left corner of the bounding box.
            ymin (int): The y-coordinate of the top left corner of the bounding box.
            xmax (int): The x-coordinate of the bottom right corner of the bounding box.
            ymax (int): The y-coordinate of the bottom right corner of the bounding box.
            args (dict, optional): A dictionary containing additional arguments. Defaults to {}.
                - type_id (str, optional): The id of the object type. Defaults to "".
                - type_name (str, optional): The name of the object type. Defaults to "".
                - score (float, optional): The confidence score of the detection. Defaults to 1..
                - super_id (int, optional): The super category id of the object type. Defaults to None.
        
        Returns:
            None.
        """
        self.xmin_ = xmin
        self.ymin_ = ymin
        self.xmax_ = xmax
        self.ymax_ = ymax
        self.type_id_ = args.get('type_id', "")
        self.type_name_ = args.get('type_name', "")
        self.score_ = args.get('score', 1.)
        self.super_id_ = args.get('super_id', None)
        self.attrs_ = [{'super_id': self.super_id_, 'id' : self.type_id_,
            'name' : self.type_name_, 'confidence' : self.score_}]
    def add_attr(self, attr):
        """
            添加属性到当前节点中。
        参数：
            - attr (str): 需要添加的属性名称，类型为字符串。
        返回值：
            - None，无返回值。
        """
        self.attrs_.append(attr)
    def __str__(self) -> str:
        """
        返回字符串格式的对象描述，包含类型ID、得分、左上角坐标和右下角坐标。
        
            Args:
                None.
        
            Returns:
                str (str): 一个字符串，包含类型ID、得分、左上角坐标和右下角坐标。格式为：
                    "{type_id_}, {score_}, {xmin_}, {ymin_}, {xmax_}, {ymax_}"。
        """
        return f"{self.type_id_}, {self.score_}, {self.xmin_}, {self.ymin_}, {self.xmax_}, {self.ymax_}"
def det_parse(info, single_filed):
    """
    解析检测信息，生成DetBox对象列表。
    """
    assert single_filed is not None, 'detection single_filed should have label'
    assert info.shape[-1] == 6, 'detection info should be [type_id, score, xmin, ymin, xmax, ymax]'
    info = info.reshape([-1, info.shape[-1]])
    print(info.shape)
    result  = []
    for box_info in info:
        if len(box_info) == 6:
            type_id, score, xmin, ymin, xmax, ymax = box_info
            type_id = int(round(float(type_id)))
            id_name = [str(type_id), str(type_id)]
            if single_filed is not None and single_filed[3] is not None:
                categories = single_filed[3]
                id_name = categories.get(type_id, [str(type_id), 'notfind'])
            result.append(DetBox(float(xmin), float(ymin), float(xmax), float(ymax), {
                "score": float(score),
                "super_id": single_filed[2],
                "type_id": id_name[0],
                "type_name": id_name[1]
            }))

    return result

def merge_box_attr(det_boxes, obj_attrs):
    """
    合并检测框和对象属性，将对象属性添加到每个检测框中。
    如果对象属性列表为空，则不进行操作。
    如果检测框列表长度不是1，则会引发异常。
    
    Args:
        det_boxes (List[List[Box3D]]): 检测框列表，包含一个检测框，形状为[[Box3D, Box3D, ...]]。
        obj_attrs (List[List[str]]): 对象属性列表，形状为[[attr1, attr2, ...], [attr1, attr2, ...], ...]。
    
    Raises:
        AssertionError: 如果检测框列表长度不是1，则会引发异常。
    
    Returns:
        None; 无返回值，直接在检测框列表中添加对象属性。
    """
    if len(obj_attrs) < 1:
        return 
    assert len(det_boxes) == 1, 'detection boxes should one'
    boxes = det_boxes[0]
    for attrs in obj_attrs:
        assert len(boxes) == len(attrs), 'detection boxes and object attrs should have same length'
        for i in range(len(boxes)):
            boxes[i].add_attr(attrs[i])
