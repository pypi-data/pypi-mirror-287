#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : generate_pre.py
"""
import os
from typing import ItemsView
import paddle_model_info
from generate_base import BaseGenerate
import other_update_pbtxt as update_pbtxt

class PreGenerate(BaseGenerate):
    """
    PreGenerate is a class that generates a pre-processing configuration file for PaddlePaddle models.
    """
    def __init__(self, config):
        """
            初始化ConfigPre类的实例，用于处理预处理后的配置文件。
        包括模板路径、输出pb.txt目录和文件名、输出模型目录等信息。
        
        Args:
            config (dict): 包含配置信息的字典，包括output_dir（输出目录）、model_version（模型版本号）等信息。
        
        Returns:
            None.
        
        Raises:
            None.
        """
        super().__init__(config)
        self.template_path = config.template_path + "/template/pre/config.pbtxt"
        self.output_pbtxt_dir = self.config.output_dir + "/pre"
        self.output_pbtxt_file = self.output_pbtxt_dir + "/config.pbtxt"
        self.output_model_dir = self.output_pbtxt_dir + "/" + self.config.model_version
        if not os.path.exists(self.output_pbtxt_dir):
            os.makedirs(self.output_pbtxt_dir)
        if not os.path.exists(self.output_model_dir):
            os.makedirs(self.output_model_dir)

    def generate(self):
        """
        generate method of the PreGenerate class.
        """
        # 读取pbtxt（作为JSON处理）  
         
        pbtxt_original = update_pbtxt.ModelConfig._create_from_file(self.template_path)
        pbtxt_dict = pbtxt_original.to_dict()

        print(pbtxt_dict)

        parameters = pbtxt_dict["optimization"]["executionAccelerators"]["cpuExecutionAccelerator"][0]["parameters"]
        print(self.config.model)
        for i in self.config.model['inputs']:
            print(i)
        print(parameters)
        
        #
        for key, value in self.config.pre_image.items():
            old_value = parameters[key]
            parameters[key] = value
            print("old_value", old_value)
            print("new_value", value)

        if 'output_image_shape' not in self.config.pre_image.keys():
            self.config.pre_image.pop('image_shape_type')
        
        if 'output_scale' in self.config.pre_image.keys():
            out_dict = {}
            out_dict['name'] = 'scale_factor'
            out_dict['data_type'] = paddle_model_info.DataType.TYPE_FP32.value
            out_dict['dims'] = [2]
            pbtxt_dict["output"].append(out_dict)
        if 'output_image_shape' in self.config.pre_image.keys():
            out_dict = {}
            out_dict['name'] = 'image_shape'
            if self.config.pre_image['image_shape_type'] ==  "float32": 
                out_dict['data_type'] = paddle_model_info.DataType.TYPE_FP32.value
            elif self.config.pre_image['image_shape_type'] ==  "int32":  
                out_dict['data_type'] = paddle_model_info.DataType.TYPE_INT32.value
            else:
                raise ValueError("image_shape_type must be float32 or int32")
            out_dict['dims'] = [2]
            pbtxt_dict["output"].append(out_dict)
        else:
            out_dict = {}
            out_dict['name'] = 'image_shape'
            out_dict['data_type'] = paddle_model_info.DataType.TYPE_FP32.value
            out_dict['dims'] = [2]
            pbtxt_dict["output"].append(out_dict)
        
        pbtxt_dict["optimization"]["executionAccelerators"]["cpuExecutionAccelerator"][0]["parameters"] = parameters
        # 
        pbtxt = update_pbtxt.ModelConfig.create_from_dictionary(pbtxt_dict)
        print(self.output_pbtxt_file)

        pbtxt.write_config_to_file(self.output_pbtxt_file)

        fw = open(self.output_model_dir + '/empty.txt', 'w')
        fw.write('没有任何用，只是空文件夹上传boost后默认删除')
        fw.close()