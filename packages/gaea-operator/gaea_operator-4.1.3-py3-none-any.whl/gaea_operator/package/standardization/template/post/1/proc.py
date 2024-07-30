#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : proc.py
"""
#coding=utf-8
import os
import json
from cv2 import threshold
import numpy as np
import yaml
import logging

import sys
import det_box
import classify_attr
#--coding:utf-8--

def get_id_by_name(name):
    """
    根据名称获取ID，如果名称不包含'|'则返回默认值0，否则返回最后一个'|'之后的整数值。如果该值小于0则输出错误信息并返回0。
    
    Args:
        name (str): 需要获取ID的名称，格式为"xxx|yyy"，其中"xxx"是任意字符串，"yyy"是一个整数。
    
    Returns:
        int: 返回获取到的ID，如果名称不包含'|'或者最后一个'|'之后的整数值小于0则返回默认值0。
    """
    vs = name.split('|')
    if len(vs) <= 1:
        # do not set, use default 0
        return 0
    else:
        int_val = int(vs[-1])
        if int_val < 0:
            print('name is invalid. name: {} invalid id: {}'.format(name, int_val))
        return int_val

def find_id_name(id_names, id):
    """
    根据ID查找对应的名称。如果未找到，则返回None。
    
    Args:
        id_names (list[tuple[int, str]]): ID和名称的列表，元组中第一个元素为ID，第二个元素为名称。
        id (int): 需要查找的ID。
    
    Returns:
        str or None: 如果找到了对应的名称，则返回该名称；否则返回None。
    """
    # logging.info('find_id_name. type: {} len: {}'.format(type(id_names[0]), len(id_names[0])))
    for _, v in enumerate(id_names):
        for _, id_name in enumerate(v):
            # logging.info('type id_name: {}'.format(type(id_name)))
            if id_name[0] == id:
                return id_name[1]
    return None

def parser_meta_json(meta_json):
    """
    解析 meta_json，返回一个包含 image_id 的列表。
    
    Args:
        meta_json (List[numpy.ndarray]): 由 numpy.ndarray 组成的列表，每个元素都是一个包含 JSON 字符串的 numpy.ndarray。
    
    Returns:
        List[int]: 包含 image_id 的列表，类型为 int。
        如果解析过程中出现任何错误（例如 JSON 格式不正确），则会引发 ValueError 异常。
    
    Raises:
        ValueError: 当解析过程中出现任何错误（例如 JSON 格式不正确）。
    """
    json_str = str(meta_json[0].tobytes())[2:-1] # delte b'
    ret_json = json.loads(json_str)
    # 1. image_id
    image_id = ret_json['image_id']
    return [image_id]


def get_yaml(yaml_name):
    """
    读取指定名称的yaml文件，并将其转换为字典格式返回。
    
    Args:
        yaml_name (str): YAML文件的路径，包括文件名。
    
    Returns:
        dict, optional: 如果成功读取YAML文件，则返回一个字典格式的数据；否则返回None。
    """
    with open(yaml_name, 'r', encoding='utf-8') as f:
        file_data = f.read()

        yaml_data = yaml.load(file_data, Loader=yaml.FullLoader)
        return yaml_data
    return None
def parser_categories(categories):
    """
    解析分类信息，返回一个字典，键为模型位置，值为一个列表，包含ID和名称。
    
    Args:
        categories (list[dict]): 每个元素是一个字典，包含'id'和'name'两个键，分别对应ID和名称。
            {'id': int, 'name': str}
    
    Returns:
        dict: 一个字典，键为模型位置，值为一个列表，包含ID和名称。{model_pos: [id, name], ...}
    """
    mapping_id_names = {}
    for model_pos,label in enumerate(categories):
        id = str(label.get('id'))
        name = str(label.get('name'))
        mapping_id_names[model_pos] = [id, name]
    return mapping_id_names
def parser_category_file(file_name):
    """
    解析类别文件，返回一个字典，键为模型位置，值为列表，包含ID和名称。
    
    Args:
        file_name (str): 类别文件的路径，相对于当前脚本的路径。
    
    Returns:
        dict or None: 如果文件不存在或解析出错，则返回None；否则返回一个字典，键为模型位置，值为列表，包含ID和名称。
    """
    mapping_id_names = {}
    file_name = os.path.dirname(__file__) + '/../' + file_name
    logging.info('category_file: {}'.format(file_name))
    print('category_file: {}'.format(file_name))
    if(os.path.exists(file_name) is False):
        logging.error('category_file not exists: {}'.format(file_name))
        print('category_file not exists: {}'.format(file_name))
        return None

    fr = open(file_name, 'r', encoding='utf-8')
    for line in fr.readlines():
        line = line.strip()
        if line.startswith('#'):
            logging.info('category_file ignore start #')
            continue
        items = line.split()
        if len(items) != 3:
            logging.error('category_file line error: {}'.format(line))
            continue
        model_pos = int(items[0])
        id = items[1]
        name = items[2]
        # print('key: {}, id: {}, name: {}'.format(model_pos, id, name))
        mapping_id_names[model_pos] = [id, name]
    return mapping_id_names
def parse_yaml_file(yaml_file_name):
    """
    解析YAML文件，返回一个元组，包含两个元素：第一个是字典类型的列表，每个元素都是一个列表，包含模型名称、输出名称、字段名称和ID名称；第二个是一个浮点数类型，表示阈值。如果解析失败或者不存在，则返回None和0.0。
    
    Args:
        yaml_file_name (str): YAML文件的路径名。
    
    Returns:
        tuple (list, float): 第一个元素是字典类型的列表，第二个元素是一个浮点数类型，分别表示字段信息和阈值。如果解析失败或者不存在，则为None和0.0。
    """
    yaml_data = get_yaml(yaml_file_name)
    threshold = 0.0
    if yaml_data != None and yaml_data.get('outputs') != None:
        ensemble_map = yaml_data['outputs'][0]
        if 'ensemble' in ensemble_map.get('model_name') and ensemble_map.get('fields_map') != None:
            fields = ensemble_map['fields_map']
            fields_list = []
            for _, field_info in enumerate(fields):
                model_name = field_info['model_name']
                field_name = field_info['field_name']
                model_out_name = field_info['model_cn_name']
                if 'threshold' in field_info.keys():
                    threshold = float(field_info['threshold'])
                id_names = None
                
                if field_name == None:
                    logging.error('yaml field invalid. field_name: {}'.format(field_name))
                    continue
                if "categories" in field_info and "category_file" in field_info:
                    logging.error('yaml field invalid. field_info only has one categories or category_file, use categories')
                if "categories" in field_info:
                    categories = field_info['categories']

                    id_names = parser_categories(categories)
                elif "category_file" in field_info:
                    id_names = parser_category_file(field_info["category_file"])
                else:
                    logging.error('field_name: {}, not has category_map'.format(field_name))
                
                fields_list.append([model_name, model_out_name, field_name, id_names])
            return fields_list, threshold
    return None, threshold
def select_field_by_name(fields_list, model_out_name):
    """
    根据字段名选择字段，如果没有找到则返回None。
    
    Args:
        fields_list (list): 包含多个元组的列表，每个元组由两个元素组成，分别是字段索引和字段名。
        model_out_name (str): 需要查找的字段名。
    
    Returns:
        tuple or None: 如果找到了对应的字段，则返回该字段的元组；否则返回None。
    """
    print("select_field_by_name field_name:{}".format(model_out_name))
    for field in fields_list:
        if model_out_name == field[1]:
            return field
    None


class Proc:
    """
    Proc类用于处理输入数据，生成输出结果。
    """
    def __init__(self, config):
        """
            init classify class
        """
        print("init classify")
        yaml_file_name = os.path.dirname(__file__) + '/../parse.yaml'
        if config.get('yaml_file_name') is not None:
            yaml_file_name = config.get('yaml_file_name')
        self.fileds_list = None
        self.threshold = 0.0
        if(os.path.exists(yaml_file_name) is True):
            print("yaml_file_name exist")
            self.fileds_list, self.threshold = parse_yaml_file(yaml_file_name)
            # print(self.fileds_list)
        assert self.fileds_list is not None, 'yaml_file_name unvalid {} '.format(yaml_file_name)
    def process(self, inputs):
        """
            处理输入数据，生成输出结果。
        该方法需要重写，提供具体的处理逻辑。
        
        Args:
            inputs (List[Dict[str, Any]]): 输入数据列表，字典中包含了不同任务的输出结果，格式如下：
                {
                    "task1": Tensor(shape=[...], dtype=float32),
                    "task2": Tensor(shape=[...], dtype=int64),
                    ...
                }
            其中key为任务名称，value为对应任务的输出结果，类型可以是Tensor或者其他支持序列化的类型。
        
        Returns:
            List[str]: 返回一个字符串列表，每个字符串都是一个JSON格式的字符串，包含了所有任务的输出结果。
        """
        outputs = []
        for input in inputs:
            categories = []
            image_ids = ["default"]
            origin_h = 0
            origin_w = 0

            det_boxes = []
            obj_attrs = []
            img_attrs = []

            for key, value in input.items():
                if 'meta_json' == key:
                    image_ids = parser_meta_json(value)
                    continue
                if 'in_scale' == key:
                    scale = value[0]
                    if scale[0] > 0.001 and scale[1] > 0.001:
                        origin_h = int(round(224.0 / scale[0]))
                        origin_w = int(round(224.0 / scale[1]))
                    continue
                if 'image_shape' == key:
                    img_shape = value[0]
                    if img_shape[0] > 0.001 and img_shape[1] > 0.001:
                        origin_h = int(round(img_shape[0]))
                        origin_w = int(round(img_shape[1]))
                    continue
                items = key.split('.')
                if len(items) >= 3 and items[0] == 'modelout':
                    if items[2] == 'detection':
                        det = det_box.det_parse(value, select_field_by_name(self.fileds_list, key))
                        det_boxes.append(det)
                    elif items[2] == 'obj_classification':
                        attr = classify_attr.classify_parse(value, select_field_by_name(self.fileds_list, key))
                        obj_attrs.append(attr)
                    elif items[2] == 'image_classification':
                        attr = classify_attr.classify_parse(value, select_field_by_name(self.fileds_list, key))
                        assert len(attr) == 1, 'image_classification len(attr) != 1'
                        img_attrs.append(attr[0])
            
            # print(det_boxes)
            # print(obj_attrs)
            # print(img_attrs)
            det_box.merge_box_attr(det_boxes, obj_attrs)

            image_info = {'image_id': image_ids[0]}

            predictions = []
            
            box_index = 0
            for i, task_box in enumerate(det_boxes):
                for j, box in enumerate(task_box):
                    print(box)
                    if box.score_ < 0.1:
                        continue
                    predict_obj = {}
                    predict_obj["bbox"] = [box.xmin_, box.ymin_, box.xmax_, box.ymax_]
                    predict_obj["confidence"] = box.score_
                    predict_obj["area"] = (box.ymax_ - box.ymin_) * (box.xmax_ - box.xmin_)
                    predict_obj['bbox_id'] = box_index
                    box_index += 1
                    predict_obj['categories'] = box.attrs_
                    predictions.append(predict_obj)
            
            if len(img_attrs) > 0:
                predict_obj = {}
                predict_obj["bbox"] = [0, 0, origin_w, origin_h]
                predict_obj["score"] = 1.0
                predict_obj["area"] = origin_h * origin_w
                predict_obj['bbox_id'] = box_index
                box_index += 1
                predict_obj['categories'] = img_attrs
                predictions.append(predict_obj)
            
            image_info['predictions'] = predictions
            json_root = [image_info] # multi images
            json_str = json.dumps(json_root)
            print(json_str)
            outputs.append(json_str)
        return outputs


if __name__ == '__main__':
    input1 = [[[1, 0.88, 10, 20, 60, 70], [1, 0.8, 10, 20, 60, 70]]]
    input2 = [[[0.1, 0.2, 0.6, 0.1], [0.2, 0.1, 0.2, 0.5]]]
    input3 = [[[0.1, 0.2, 0.7]]]
    inputs = [{"modelout.0.detection": np.array(input1), "modelout.2.obj_classification": np.array(input2), "modelout.3.image_classification": np.array(input3)}]
    proc = Proc({'yaml_file_name': "../parse.yaml"})
    proc.process(inputs)