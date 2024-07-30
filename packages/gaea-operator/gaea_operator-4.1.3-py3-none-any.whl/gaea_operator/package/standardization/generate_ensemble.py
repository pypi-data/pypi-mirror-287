#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : generate_ensemble.py
"""
import os
from generate_base import BaseGenerate
import other_update_pbtxt as update_pbtxt

class EnsembleGenerate(BaseGenerate):
    """
    EnsembleGenerate is a class that inherits from BaseGenerate and is used to generate the ensemble configuration file.
    """
    def __init__(self, config):
        """
            Initializes the EnsembleConfig object.
        
        Args:
            config (dict): A dictionary containing configuration parameters for the ensemble model.
                Required keys are:
                    - output_dir (str): The directory where the ensemble model will be saved.
                    - model_version (str): The version of the ensemble model.
        
        Raises:
            KeyError: If required configuration parameters are missing from the input dictionary.
        """
        super().__init__(config)
        self.template_path = config.template_path + "/template/ensemble/config.pbtxt"
        self.output_pbtxt_dir = self.config.output_dir + "/ensemble"
        self.output_pbtxt_file = self.output_pbtxt_dir + "/config.pbtxt"
        self.output_model_dir = self.output_pbtxt_dir + "/" + self.config.model_version
        if not os.path.exists(self.output_pbtxt_dir):
            os.makedirs(self.output_pbtxt_dir)
        if not os.path.exists(self.output_model_dir):
            os.makedirs(self.output_model_dir)

    def generate(self):
        """
        generate method of EnsembleGenerate class which generates the ensemble configuration file.
        """
        # 读取pbtxt（作为JSON处理）  
         
        pbtxt_original = update_pbtxt.ModelConfig._create_from_file(self.template_path)
        pbtxt_dict = pbtxt_original.to_dict()

        # pbtxt_dict["input"] = []
        # pbtxt_dict["output"] = []
        # for i in self.config.model['inputs']:
            
        #     input_dict = {"name": i['name'], "dims": i['dims'][1:], "data_type": i['data_type']}
        #     pbtxt_dict["input"].append(input_dict)
        
        # for index  in self.config.need_output_indexs:
        #     config_output_dict = self.config.model["outputs"][index]
        #     output_dict = {"name": config_output_dict['name'], "dims": config_output_dict['dims'][1:], "data_type": config_output_dict['data_type']}
        #     pbtxt_dict["output"].append(output_dict)

        # print(pbtxt_dict['ensembleScheduling']['step'][0]['outputMap'])

        if 'output_scale' in self.config.pre_image.keys():
            pbtxt_dict['ensembleScheduling']['step'][0]['outputMap']['scale_factor'] = 'scale_factor'
        # if 'output_image_shape' in self.config.pre_image.keys():
        pbtxt_dict['ensembleScheduling']['step'][0]['outputMap']['image_shape'] = 'image_shape'
        
        pbtxt_dict['ensembleScheduling']['step'][1]['inputMap'].clear()
        for model_name, name in self.config.ensemble['pre_infer'].items():
            pbtxt_dict['ensembleScheduling']['step'][1]['inputMap'][model_name] = name
        
        pbtxt_dict['ensembleScheduling']['step'][1]['outputMap'].clear()
        for index in self.config.need_output_indexs:
            config_output_dict = self.config.model["outputs"][index]
            pbtxt_dict['ensembleScheduling']['step'][1]['outputMap'][config_output_dict['name']] \
                = self.config.post[index].out_label_name
        
        post_input = pbtxt_dict['ensembleScheduling']['step'][1]['outputMap'].values()

        # pbtxt_dict['ensembleScheduling']['step'][2]['inputMap'].clear()
        for name in post_input:
            pbtxt_dict['ensembleScheduling']['step'][2]['inputMap'][name] = name
        pbtxt_dict['ensembleScheduling']['step'][2]['inputMap']['image_shape'] = 'image_shape'

        pbtxt = update_pbtxt.ModelConfig.create_from_dictionary(pbtxt_dict)
        # print(self.output_pbtxt_file)

        pbtxt.write_config_to_file(self.output_pbtxt_file)

        fw = open(self.output_model_dir + '/empty.txt', 'w')
        fw.write('没有任何用，只是空文件夹上传boost后默认删除')
        fw.close()

