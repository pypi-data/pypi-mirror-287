#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : model_config.py
"""
import os
import yaml
import paddle_model_info
import shutil
#from ppdet.core.config.yaml_helpers import serializable

class ModelConfig():
    """
    ModelConfig is the config of model, it contains model_file_name, params_file_name, pre_image, model, post, ensemble
    """
    class PostInputInfo():
        """
        PostInputInfo is the input info of post
        """
        out_index = 0
        out_label_name = ''
        out_shape = []
        task_type = ''
        super_id = ''
        categories = {}
        def __str__(self):
            """
                返回一个字符串，包含了该对象的所有信息。
            这个方法被Python内置函数print()调用，以将对象转换为字符串输出。
            
            Returns:
                str -- 一个包含了该对象所有信息的字符串。
            """
            info = "out_index:" + str(self.out_index) \
                + ", out_label_name:" + self.out_label_name \
                + ", out_shape:" + str(self.out_shape) \
                + ", task_type:" + self.task_type + ", super_id:" + self.super_id
            for k, v in self.categories.items():
                info += ", categories " + str(k) + ":" + ','.join([str(i) for i in v])
            return info

    output_dir = ""
    model_version = "1"
    def __init__(self, config_file, model_dir, output_dir):
        """
            Initialization method for the class.
        
        Args:
            config_file (str): Path to the configuration file.
            model_dir (str): Path to the directory containing the pre-trained model.
            output_dir (str): Path to the directory where the results will be saved.
        
        Raises:
            AssertionError: If the model or parameter files are not found.
        """
        self.det_threshold = 0.1
        self.config_name = config_file
        self.config_name_modify = config_file + ".tmp"
        self.model_name = "test"
        self.template_path = os.path.dirname(__file__)
        self.pre_image = {}
        self.model = {}
        self.post = {}
        self.ensemble = {}

        self.need_output_indexs = None
        
        model_dir = model_dir.rstrip('/')
        if os.path.exists(model_dir + "/__model__"):
            self.model_file_name = model_dir + "/__model__"
        else:
            self.model_file_name = model_dir + "/model.pdmodel"
        if os.path.exists(model_dir + "/__params__"):
            self.params_file_name = model_dir + "/__params__"
        else:
            self.params_file_name = model_dir + "/model.pdiparams"
        
        assert os.path.exists(self.model_file_name), self.model_file_name + " not found"
        assert os.path.exists(self.params_file_name), self.params_file_name + " model.pdiparams not found"

        self.output_dir = output_dir.rstrip('/')

    def Parse(self):
        """
        Parse parse the model config file
        """
        paddle_model_obj =  paddle_model_info.PaddleModel(self.model_file_name, self.params_file_name)
        model_meta = paddle_model_obj.info()
        for key, value in model_meta.items():
            # print('key: ', key, 'value: ', value)
            self.model[key] = value
        with open(self.config_name) as f:
            content=[]
            tag = 0
            for line in f.readlines():
                tag = tag + 1
                line = line.strip('\n')
                char_index = line.find('!')
                if char_index != -1:
                    if ':' in line[:char_index]:
                        line = line.replace('!', '#')
                    elif '-' in line[:char_index]:
                        line = line[:char_index] + "key" + str(tag) + ": value" + str(tag)
                    else:
                        line = line
                else:
                    line = line
                #print(line)
                content.append(line)
            fw = open(self.config_name_modify, 'w')
            content_str = '\n'.join(str(item) for item in content)
            #print(type(content_str))
            fw.write(content_str)
            fw.close()

        with open(self.config_name_modify) as f:
            dataMap = yaml.safe_load(f)
            
            print(dataMap['TestReader']['sample_transforms'])
            for it in dataMap['TestReader']['sample_transforms']:
                if 'Resize' in it.keys():
                    if it['Resize']['interp'] == 0:
                        self.pre_image["interp"] = "nearest"
                    elif it['Resize']['interp'] == 1:
                        self.pre_image["interp"] = "bilinear"
                    else:
                        raise Exception("unsupport data type")
                elif 'NormalizeImage' in it.keys():
                    #归一化参数默认是按rgb给出,转入后按bgr给出
                    mean = it['NormalizeImage']['mean']
                    std = it['NormalizeImage']['std']
                    assert len(mean) == 3 and len(std) == 3, "mean std must be three"
                    mean[0], mean[2] = mean[2], mean[0]
                    std[0], std[2] = std[2], std[0]
                    self.pre_image["mean_bgr"] = ','.join([str(x) for x in mean])
                    self.pre_image["std_bgr"] = ','.join([str(x) for x in std]) 
            
            assert len(dataMap['tasks']) + 1 == len(self.model['outputs']), \
                "tasks num {}  + 1 must be equal to model outputs num {}".format(\
                len(dataMap['tasks']), len(self.model['outputs']))
            out_index = 0
            for it in dataMap['tasks']: # detect 任务占用模型的两个输出，留出第一通道输出，不解析
                info = ModelConfig.PostInputInfo()
                info.out_index = out_index
                info.super_id = it['task_name']
                info.task_type = it['task_type']
                info.out_label_name = 'modelout.' + str(out_index) + '.' + it['task_type']
                categories = {}
                argmax_index = 0
                for k, v in it['categories'].items():
                    categories[argmax_index] = [k, v]
                    argmax_index += 1
                info.categories = categories
                self.post[out_index] = info
                out_index += 1
                if out_index == 1:
                    out_index += 1
        for key, value in self.post.items():
            print(value)
        self.need_output_indexs = self.post.keys()

        self.pre_image["channel_order"] = "rgb" #标准化训练，默认使用rgb
        
        pre_output = {}
        num_inputs = {"image_shape": 0, "scale_factor": 0, "preprocessed_image": 0}
        for i in self.model["inputs"]:
            input_dict = {"name": i['name'], "dims": i['dims'][1:], "data_type": i['data_type']}
            name = ''
            if i['name'] == "image_shape":
                name = "image_shape"
            elif i['name'] == "scale_factor":
                name = "scale_factor"
            else: 
                name = "preprocessed_image"
            
            data_type = ''
            if i['data_type'] == paddle_model_info.DataType.TYPE_FP32.value:
                data_type = "float32"
            elif i['data_type'] == paddle_model_info.DataType.TYPE_INT32.value:
                data_type = "int32"
            else:
                print(i['data_type'])
                raise Exception("unsupport data type")
            
            pre_output[name] = {"name": name, "out_shape": i['dims'][1:],
                "image_shape_type": data_type, "model_name": i['name']}
            num_inputs[name] += 1
        print(num_inputs)
        assert num_inputs["preprocessed_image"] == 1, "only support one preprocessed_image"
        assert num_inputs["image_shape"] <= 1, "only support lower one image_shape"
        assert num_inputs["scale_factor"] <= 1, "only support lower one scale_factor"

        self.pre_image["out_shape"] = ','.join([str(x) for x in pre_output['preprocessed_image']['out_shape']])

        if 'image_shape' in pre_output.keys():
            self.pre_image["output_image_shape"] = 'image_shape'
            self.pre_image["image_shape_type"] = pre_output['image_shape']['image_shape_type']
        if 'scale_factor' in pre_output.keys():
            self.pre_image["output_scale"] = 'scale_factor'

        self.ensemble['pre_infer'] = {}
        for it in pre_output.values():
            self.ensemble['pre_infer'][it['model_name']] = it['name']
        
        self.output_dir = self.output_dir + '/' + self.model_name
        if os.path.exists(self.output_dir):  
            shutil.rmtree(self.output_dir)  # 删除文件夹
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        return
