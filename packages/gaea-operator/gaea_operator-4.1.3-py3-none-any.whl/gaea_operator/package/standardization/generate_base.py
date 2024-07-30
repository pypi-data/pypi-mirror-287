#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/7/9
# @Author  : xumingyang02
# @File    : generate_base.py
"""


class BaseGenerate():
    """
    BaseGenerate is the base class for generating data
    """
    def __init__(self, config):
        """
            Initializes the instance with the given configuration.
        
        Args:
            config (dict): A dictionary containing the configuration parameters.
                           The keys of this dictionary are the names of the
                           configuration options and the values are the values
                           for those options.
        """
        self.config = config

    def generate(self):
        """
        inferface for generating data
        """
        pass
