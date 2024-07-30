# Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : model.py
"""
import logging
import os
import json
import numpy as np
import time
# triton_python_backend_utils is available in every Triton Python model. You
# need to use this module to create inference requests and responses. It also
# contains some utility functions for extracting information from model_config
# and converting Triton input/output types to numpy types.
import triton_python_backend_utils as pb_utils
import proc

class TritonPythonModel:
    """Your Python model must use the same class name. Every Python model
    that is created must have "TritonPythonModel" as the class name.
    """

    def initialize(self, args):
        """`initialize` is called only once when the model is being loaded.
        Implementing `initialize` function is optional. This function allows
        the model to intialize any state associated with this model.

        Parameters
        ----------
        args : dict
          Both keys and values are strings. The dictionary keys and values are:
          * model_config: A JSON string containing the model configuration
          * model_instance_kind: A string containing model instance kind
          * model_instance_device_id: A string containing model instance device ID
          * model_repository: Model repository path
          * model_version: Model version
          * model_name: Model name
        """
        self.dst_path = os.getenv('ENV_RET_PATH')
        if self.dst_path is None or len(self.dst_path) <= 0:
            self.dst_path = '/root/skill_log'
        if(os.path.exists(self.dst_path) is False):
            os.makedirs(self.dst_path)
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(pathname)s(%(lineno)d) - %(message)s"
        logging.basicConfig(
            format = LOG_FORMAT,
            # datefmt='',
            filename=self.dst_path + '/skill.log',
            level=logging.INFO
        )

        # 1. get outputs type
        self.model_config = model_config = json.loads(args['model_config'])
        self.input_names = []
        if "input" in model_config:
            inputs = model_config["input"]
            for input_properties in inputs:
                self.input_names.append(input_properties["name"])
                                        
        if "output" in model_config:
            outputs = model_config["output"]
            self.output_names = []
            self.output_dtype = []
            for output_properties in outputs:
                self.output_names.append(output_properties["name"])
                self.output_dtype.append(pb_utils.triton_string_to_numpy(output_properties['data_type']))
        if len(self.output_names) != 1:
            logging.error('output num {} not support, only support 1 output.'.format(len(self.output_names)))
        logging.info('output name {}, out_type {}'.format(self.output_names[0], self.output_dtype[0]))

        

        self.proc = proc.Proc(model_config)

    def request_2_input(self, requests):
        """
            获取输入数据，返回一个列表，每个元素是一个字典，包含所有输入名称对应的numpy数组。
        如果某个输入不能获取到tensor，则跳过该输入。
        
        Args:
            requests (List[InferenceRequest]): 包含多个InferenceRequest对象，每个对象代表一次推理请求。
        
        Returns:
            List[Dict[str, numpy.ndarray]]: 包含多个字典，每个字典包含所有输入名称对应的numpy数组。
            如果某个输入不能获取到tensor，则该字典中对应的键值对为None。
        """
        inputs = []
        for req in requests:
            inp = {}
            for key in self.input_names:
                in_tensor = pb_utils.get_input_tensor_by_name(req, key)
                if in_tensor is None:
                    logging.error('{} input can not get tensor.'.format(key))
                    continue
                # print(in_tensor.as_numpy())
                inp[key] = in_tensor.as_numpy()
            inputs.append(inp)
        return inputs
    def execute(self, requests):
        """`execute` MUST be implemented in every Python model. `execute`
        function receives a list of pb_utils.InferenceRequest as the only
        argument. This function is called when an inference request is made
        for this model. Depending on the batching configuration (e.g. Dynamic
        Batching) used, `requests` may contain multiple requests. Every
        Python model, must create one pb_utils.InferenceResponse for every
        pb_utils.InferenceRequest in `requests`. If there is an error, you can
        set the error argument when creating a pb_utils.InferenceResponse

        Parameters
        ----------
        requests : list
          A list of pb_utils.InferenceRequest

        Returns
        -------
        list
          A list of pb_utils.InferenceResponse. The length of this list must
          be the same as `requests`
        """
        start_time = time.time()
        responses = []

        # Every Python backend must iterate over everyone of the requests
        # and create a pb_utils.InferenceResponse for each of them.
        inputs = self.request_2_input(requests)

        convert_time = time.time()
        outputs = self.proc.process(inputs)
        proc_time = time.time()
        for output in outputs:
            # logging.info('skill postproc begin. get names')
            out_tensors = []
            # for json_str in output:
            # print(self.output_names[0])
            # print(self.output_dtype[0])
            output_tensor_json = pb_utils.Tensor(self.output_names[0], np.fromstring(output, self.output_dtype[0]))
            out_tensors.append(output_tensor_json)

            inference_response = pb_utils.InferenceResponse(output_tensors=out_tensors)

            responses.append(inference_response)

        # You should return a list of pb_utils.InferenceResponse. Length
        # of this list must match the length of `requests` list.
        end_time = time.time()
        logging.info('skill postproc runtime {}, convert runtime {}, proc runtime {}'.format(
            end_time - start_time, convert_time - start_time, proc_time - convert_time))
        return responses

    def finalize(self):
        """`finalize` is called only once when the model is being unloaded.
        Implementing `finalize` function is OPTIONAL. This function allows
        the model to perform any necessary clean ups before exit.
        """
        print('Cleaning up...')
