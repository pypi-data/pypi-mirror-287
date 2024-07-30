#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : paddle_model_info.py
"""
import sys
import paddle.inference as paddle_infer
import numpy as np
import paddle.base.proto.framework_pb2 as framework_pb2
# import paddle.fluid.proto.framework_pb2 as framework_pb2
from enum import Enum  
  
class DataType(Enum):
    """
    Data type of the tensor.
    """
    TYPE_BOOL = 1
    TYPE_UINT8 = 2
    TYPE_UINT16 = 3
    TYPE_UINT32 = 4
    TYPE_UINT64 = 5
    TYPE_INT8 = 6
    TYPE_INT16 = 7
    TYPE_INT32 = 8
    TYPE_INT64 = 9
    TYPE_FP16 = 10
    TYPE_FP32 = 11
    TYPE_FP64 = 12
    TYPE_STRING = 13
    TYPE_BF16 = 14
    # INT32 = 2;
    # INT64 = 3;
    # FP32 = 5;
class PaddleModel():
    """
    Paddle Model Info Class
    """
    def __init__(self, model_file, params_file):
        """
            初始化函数，用于设置模型文件和参数文件路径。
        
        Args:
            model_file (str): 模型文件的路径。
            params_file (str): 参数文件的路径。
        
        Returns:
            None.
        
        Raises:
            None.
        """
        self.model_file = model_file
        self.params_file = params_file
        self.out_indexs = None
        self.batch_size = 1
    def info(self):
        """
        print model information
        """
        # 创建 config
        config = paddle_infer.Config(self.model_file, self.params_file)

        # 根据 config 创建 predictor
        predictor = paddle_infer.create_predictor(config)

        # 获取输入的名称
        input_names = predictor.get_input_names()
        # for name in input_names:
        #     print('Input Name：{}'.format(name))
        #     input_handle = predictor.get_input_handle(name)
        #     print("\tType：", input_handle.type())
        #     print("\tShape：", input_handle.shape())
        
        output_names = predictor.get_output_names()
        print('int32 num need ignore: {}'.format(output_names[1]))

        fr = open(self.model_file, 'rb')
        x = fr.read()

        m = framework_pb2.ProgramDesc.FromString(x)
        # print(m)
        print(m.version)
        # print(m.op_version_map)
        # print('block len: {}'.format(len(m.blocks)))
        meta_data={"inputs" : [None] * len(input_names), "outputs" : [None] * len(output_names)}
        for b in m.blocks:
            # print(b.idx)
            # print(b.parent_idx)
            print('vars len: {}'.format(len(b.vars)))
            for v in b.vars:
                data_type = v.type.lod_tensor.tensor.data_type
                if data_type == 2:
                    data_type = DataType.TYPE_INT32
                elif data_type == 3:
                    data_type = DataType.TYPE_INT64
                elif data_type == 5:
                    data_type = DataType.TYPE_FP32
                elif data_type == 0:
                    data_type = DataType.TYPE_BOOL
                else:
                    print(data_type)
                    raise Exception("unknow data type")
                if v.name in input_names:
                    index = input_names.index(v.name)
                    meta_data["inputs"][index] = {'name': v.name, 'data_type': data_type.value, \
                        'dims': v.type.lod_tensor.tensor.dims}
                elif v.name in output_names:
                    index = output_names.index(v.name)
                    meta_data["outputs"][index] = {'name': v.name, 'data_type': data_type.value, \
                        'dims': v.type.lod_tensor.tensor.dims}

                # print(v)
                # break
            # print('ops len: {}'.format(len(b.ops)))
            # # for op in b.ops:
            # #     print(op)
            # #     break
            # print(b.forward_block_idx)
            break
        return meta_data

if __name__ == "__main__":
    print("Hello World")
    inf = PaddleModel('/home/xumingyang02/code/tmp_model/__model__', \
        '/home/xumingyang02/code/tmp_model/__params__')
    meta = inf.info()
    print(meta)