#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : generate_infer.py
"""
import os
import shutil 
from generate_base import BaseGenerate

import other_update_pbtxt as update_pbtxt

class InferGenerate(BaseGenerate):
    """
    InferGenerate is a class that inherits from BaseGenerate.
    """
    def __init__(self, config):
        """
            初始化InferConfig类的实例，用于生成模型推理所需的配置文件。
        
        Args:
            config (dict): 包含模型推理所需信息的字典，包括输出目录、模型版本等信息。
                - output_dir (str, optional): 输出目录路径，默认为"./"。
                - model_version (str, optional): 模型版本号，默认为"1.0"。
        
        Returns:
            None.
        
        Raises:
            None.
        """
        super().__init__(config)
        self.template_path = config.template_path + "/template/infer/config.pbtxt"
        self.output_pbtxt_dir = self.config.output_dir + "/infer"
        self.output_pbtxt_file = self.output_pbtxt_dir + "/config.pbtxt"
        self.output_model_dir = self.output_pbtxt_dir + "/" + self.config.model_version

        if not os.path.exists(self.output_pbtxt_dir):
            os.makedirs(self.output_pbtxt_dir)
        if not os.path.exists(self.output_model_dir):
            os.makedirs(self.output_model_dir)

    def generate(self):
        """
        This function generates the inference configuration file and copies the model files to the specified directory.
        """
        # 读取pbtxt（作为JSON处理）  
         
        pbtxt_original = update_pbtxt.ModelConfig._create_from_file(self.template_path)
        pbtxt_dict = pbtxt_original.to_dict()

        pbtxt_dict["input"] = []
        pbtxt_dict["output"] = []
        for i in self.config.model['inputs']:
            
            input_dict = {"name": i['name'], "dims": i['dims'][1:], "data_type": i['data_type']}
            pbtxt_dict["input"].append(input_dict)
        
        print('need_output_indexs: {}'.format(','.join([str(i) for i in self.config.need_output_indexs])))
        for index  in self.config.need_output_indexs:
            config_output_dict = self.config.model["outputs"][index]
            output_dict = {
                "name": config_output_dict['name'], 
                "dims": config_output_dict['dims'][:], 
                "data_type": config_output_dict['data_type']}
            pbtxt_dict["output"].append(output_dict)

        print(pbtxt_dict)
        # 
        pbtxt = update_pbtxt.ModelConfig.create_from_dictionary(pbtxt_dict)
        # print(self.output_pbtxt_file)

        pbtxt.write_config_to_file(self.output_pbtxt_file)

        # 使用shutil.copy()拷贝文件  
        try:  
            shutil.copy(self.config.model_file_name, self.output_model_dir + "/model.pdmodel")  # 拷贝文件  
            shutil.copy(self.config.params_file_name, self.output_model_dir + "/model.pdiparams")  # 拷贝文件  
        except FileNotFoundError:  
            print(f"源文件 不存在！")  
        except PermissionError:  
            print(f"没有足够的权限来拷贝文件！")  
        except Exception as e:  
            print(f"拷贝文件时发生错误: {e}")

        
        return True



if __name__ == "__main__":
    ge = InferGenerate(None)
    ge.generate()

