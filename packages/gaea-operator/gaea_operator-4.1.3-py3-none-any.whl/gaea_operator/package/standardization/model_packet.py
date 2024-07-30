#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : model_packet.py
"""
from requests import post
import model_config
import sys
import argparse  
import paddle_model_info
import generate_infer
import generate_pre
import generate_post
import generate_ensemble

def packet(config_name, model_dir, output_dir):
    """
    打包模型,生成paddle仓库所需的文件
    """
    config = model_config.ModelConfig(config_name, model_dir, output_dir)
    config.Parse()

    infer_handler = generate_infer.InferGenerate(config)
    pre_handler = generate_pre.PreGenerate(config)
    post_handler = generate_post.PostGenerate(config)
    ensemble_handler = generate_ensemble.EnsembleGenerate(config)

    handlers = [infer_handler, pre_handler, post_handler, ensemble_handler]

    for handler in handlers:
        handler.generate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple example with argparse")  
    parser.add_argument("--config_file", type=str, help="config_file argument")  
    parser.add_argument("--model_dir", type=str, help="model_dir argument")
    parser.add_argument("--output_dir", type=str, default="./model_repo", help="output_dir argument")  
  
    args = parser.parse_args()  
  
    packet(args.config_file, args.model_dir, args.output_dir)