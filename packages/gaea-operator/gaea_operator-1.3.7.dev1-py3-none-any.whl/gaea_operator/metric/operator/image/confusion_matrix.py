#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File          : confusion_matrix.py    
@Author        : yanxiaodong
@Date          : 2023/5/25
@Description   :
"""
from typing import List, Union, Optional, Any
import numpy as np

from gaea_operator.utils import paddle, torch, PTensor, TTensor, Tensor
from ..metric import MetricOperator
from gaea_operator.utils import METRIC
from ..check import check_input_dim, check_input_type, check_input_num_classes
from gaea_operator.utils import list2ndarray


@METRIC.register_module('confusion_matrix')
class ConfusionMatrix(MetricOperator):
    """
    Confusion matrix of the evaluation.
    """
    metric_name = 'confusion_matrix'

    def __init__(self, thresholds: Optional[float] = 0.5, **kwargs):
        super(ConfusionMatrix, self).__init__(num_classes=kwargs.get('num_classes', 2))

        self.thresholds = thresholds
        if self.name in kwargs:
            self.thresholds = float(kwargs[self.name]['thresholds'])

        self.add_state("confmat", default=0)

    def update(self, predictions: Union[List, Tensor], references: Union[List, Tensor]) -> None:
        """
        Computes and returns the middle states, such as TP, etc.
        """
        check_input_type(predictions=predictions, references=references)

        predictions = list2ndarray(predictions)
        references = list2ndarray(references)

        check_input_dim(predictions=predictions, num_classes=self.num_classes)

        if isinstance(predictions, np.ndarray):
            if self.num_classes == 2:
                if not all((predictions == 1) | (predictions == 0)):
                    predictions = (predictions >= self.thresholds).astype(np.int32)
            else:
                if not predictions.ndim == 1:
                    check_input_num_classes(predictions=predictions, num_classes=self.num_classes)

                    predictions = predictions.argmax(axis=1)

            unique_mapping = references * self.num_classes + predictions
            bins = np.bincount(unique_mapping, minlength=self.num_classes ** 2)
            confmat = bins.reshape(self.num_classes, self.num_classes)

            self.confmat += confmat

        if isinstance(predictions, PTensor):
            if self.num_classes == 2:
                if not paddle.all((predictions == 1) | (predictions == 0)):
                    predictions = (predictions >= self.thresholds).cast(paddle.int32)
            else:
                if not predictions.ndim == 1:
                    check_input_num_classes(predictions=predictions, num_classes=self.num_classes)

                    predictions = paddle.argmax(predictions, axis=1)

            unique_mapping = references * self.num_classes + predictions
            # bins = paddle.bincount(unique_mapping, minlength=self.num_classes ** 2)
            bins = np.bincount(unique_mapping.numpy(), minlength=self.num_classes ** 2)
            bins = paddle.to_tensor(bins)
            confmat = bins.reshape((self.num_classes, self.num_classes))

            self.confmat += confmat

        if isinstance(predictions, TTensor):
            if self.num_classes == 2:
                if not torch.all((predictions == 1) | (predictions == 0)):
                    predictions = (predictions >= self.thresholds).int()
            else:
                if not predictions.ndim == 1:
                    check_input_num_classes(predictions=predictions, num_classes=self.num_classes)

                    predictions = torch.argmax(predictions, dim=1)

            unique_mapping = references * self.num_classes + predictions
            bins = torch.bincount(unique_mapping, minlength=self.num_classes ** 2)
            confmat = bins.reshape(self.num_classes, self.num_classes)

            self.confmat += confmat

    def compute(self) -> Any:
        """
        Computes the metric by middle states.
        """
        return self.confmat.tolist()



