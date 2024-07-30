#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
  ████
██    ██   Datature
  ██  ██   Powering Breakthrough AI
    ██

@File    :   __init__.py
@Author  :   Wei Loon Cheng
@Version :   1.7.2
@Contact :   developers@datature.io
@License :   Apache License 2.0
@Desc    :   TensorRT init module
"""

from .tensorrt import TensorRTConverter

# Expose certain elements at package level
__all__ = ["TensorRTConverter"]
