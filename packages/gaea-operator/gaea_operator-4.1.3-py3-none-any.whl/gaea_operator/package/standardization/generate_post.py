#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : generate_post.py
"""
import os
from turtle import update
import paddle_model_info
from generate_base import BaseGenerate
import other_update_pbtxt as update_pbtxt
import other_update_parse as update_parse
import shutil

class PostGenerate(BaseGenerate):
    """
    PostGenerate class is used to generate post model config file
    """
    def __init__(self, config):
        """
            Initializes the PostProcessor class.
        
        Args:
            config (Config): An instance of Config class containing configuration parameters.
        
        Returns:
            None.
        
        Raises:
            None.
        """
        super().__init__(config)
        self.template_model_path = config.template_path + "/template/post/1"
        self.template_path = config.template_path + "/template/post/config.pbtxt"
        self.template_parse_path = config.template_path + "/template/post/parse.yaml"
        self.output_pbtxt_dir = self.config.output_dir + "/post"
        self.output_pbtxt_file = self.output_pbtxt_dir + "/config.pbtxt"
        self.output_yaml_file = self.output_pbtxt_dir + "/parse.yaml"
        self.output_model_dir = self.output_pbtxt_dir + "/" + self.config.model_version
        if not os.path.exists(self.output_pbtxt_dir):
            os.makedirs(self.output_pbtxt_dir)

    def generate(self):
        """
        generate method is used to generate post model config file and parse yaml file
        """
        pbtxt_original = update_pbtxt.ModelConfig._create_from_file(self.template_path)
        pbtxt_dict = pbtxt_original.to_dict()

        for index  in self.config.need_output_indexs:
            config_output_dict = self.config.model["outputs"][index]
            output_dict = {"name": self.config.post[index].out_label_name,
                "dims": config_output_dict['dims'][:], "data_type": config_output_dict['data_type']}
            pbtxt_dict["input"].append(output_dict)
        
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
            pbtxt_dict["input"].append(out_dict)
        else:
            out_dict = {}
            out_dict['name'] = 'image_shape'
            out_dict['data_type'] = paddle_model_info.DataType.TYPE_FP32.value
            out_dict['dims'] = [2]
            pbtxt_dict["input"].append(out_dict)

        print(pbtxt_dict)
        # 
        pbtxt = update_pbtxt.ModelConfig.create_from_dictionary(pbtxt_dict)
        # print(self.output_pbtxt_file)

        pbtxt.write_config_to_file(self.output_pbtxt_file)

        parse_origin = update_parse.ParseYamlConfig(self.template_parse_path)

        fields_map = []
        for key in self.config.post.keys():
            # print(self.config.post[index])
            attr_map = {}
            assert key == self.config.post[key].out_index, "nedd equal"
            attr_map["field_name"] = self.config.post[key].super_id
            attr_map["model_name"] = self.config.model_name
            attr_map["model_type"] = self.config.post[key].task_type
            attr_map["model_cn_name"] = self.config.post[key].out_label_name
            if 'detection' in self.config.post[key].task_type:
                attr_map["threshold"] = self.config.det_threshold
            
            categories = []
            for category_index in range(len(self.config.post[key].categories.keys())):
                label_map = {}
                assert category_index == len(categories), "nedd equal"
                cate_key = category_index
                label_map["id"] = self.config.post[key].categories[cate_key][0]
                label_map["name"] = self.config.post[key].categories[cate_key][1]
                categories.append(label_map)
            attr_map["categories"] = categories

            fields_map.append(attr_map)
        
        parse_origin.set_fields_map(fields_map)
        parse_origin.save_yaml(self.output_yaml_file)
        
        # 使用shutil.copy()拷贝文件  
        try:  
            if os.path.exists(self.output_model_dir):  
                shutil.rmtree(self.output_model_dir)  # 删除文件夹  
            shutil.copytree(self.template_model_path, self.output_model_dir)  # 拷贝文件  
        except FileNotFoundError:  
            print(f"源文件 不存在！")  
        except PermissionError:  
            print(f"没有足够的权限来拷贝文件！")  
        except Exception as e:  
            print(f"拷贝文件时发生错误: {e}")

