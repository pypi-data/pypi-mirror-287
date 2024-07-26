# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
"""
modify input train parameter yaml
Authors: wanggaofei(wanggaofei03@baidu.com)
Date:    2023-02-29
"""
import os
import yaml

import bcelogger

from gaea_operator.config.config import get_pretrained_model_path, set_multi_key_value
from gaea_operator.utils import write_yaml_file

KEY_EVAL_HEIGHT = 'eval_height'
KEY_EVAL_WIDTH = 'eval_width'
KEY_TEXT_SCENE = 'text_scene'


def generate_train_config(
        advanced_parameters: dict,
        pretrain_model_uri: str,
        train_config_name: str
):
    """
        modify parameter by template config
    """
    # 0. modify width/height var
    width = advanced_parameters[KEY_EVAL_WIDTH]
    height = advanced_parameters[KEY_EVAL_HEIGHT]
    advanced_parameters["Train.dataset.transforms.RecResizeImg.image_shape"] = [height, width, 3]
    advanced_parameters["Train.dataset.transforms.sampler.scales"] = [[width, height - 16],
                                                                      [width, height],
                                                                      [width, height + 16]]
    advanced_parameters["Eval.dataset.transforms.RecResizeImg.image_shape"] = [3, height, width]

    if advanced_parameters[KEY_TEXT_SCENE].endswith('english'):
        config_filename = 'parameter_english.yaml'
    else:
        config_filename = 'parameter_chinese.yaml'

    bcelogger.info('train parameter name: {}'.format(config_filename))

    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_filename)
    with open(config_file) as f:
        config_data = yaml.load(f, Loader=yaml.Loader)

    # get model pretrain model path
    paths = get_pretrained_model_path(pretrain_model_uri)
    advanced_parameters["Global.pretrained_model"] = paths[0] if len(paths) > 1 else None

    for key, val in advanced_parameters.items():
        set_multi_key_value(config_data, key, val)

    bcelogger.info('begin to save yaml. {}'.format(train_config_name))
    write_yaml_file(config_data, os.path.dirname(train_config_name), os.path.basename(train_config_name))
    bcelogger.info('write train config finish.')