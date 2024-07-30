#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : classify_parse.py
"""
#coding=utf-8
import os
import json
import numpy as np
import yaml
import logging

import sys

#--coding:utf-8--
def classify_parse(info, single_filed):
    """
    对输入的信息进行分类，并返回每个类别的属性值。
    
    Args:
        info (np.ndarray, list or tuple): 包含多个特征向量的numpy数组或者列表或元组，其中每个特征向量是一个长度为n的向量，n为特征数。
        single_filed (list or tuple, optional): 包含三个元素的列表或元组，第一个元素是label，第二个元素是id，第三个元素是categories（可选）。默认为None，不需要label。
    
    Returns:
        list: 包含每个类别的属性值，包括super_id、id、name和confidence，以字典形式存储。
    
    Raises:
        AssertionError: 当single_filed不为None且单元格中没有label时会引发该错误。
    """
    assert single_filed is not None, 'classify_parse single_filed should have label'
    info = info.reshape([-1, info.shape[-1]])
    print(info.shape)
    attrs = []
    for values in info:
        max_pos = np.argmax(values)
        max_pos = max_pos
        # print('max_pos {}'.format(max_pos))
        
        max = float(values[max_pos])
        id_name = [str(max_pos), str(max_pos)]
        if single_filed is not None and single_filed[3] is not None:
            categories = single_filed[3]
            id_name = categories.get(max_pos, [str(max_pos), 'notfind'])
        attr ={'super_id': single_filed[2], 'id': id_name[0], 'name': id_name[1], 'confidence': max}
        attrs.append(attr)
    return attrs
