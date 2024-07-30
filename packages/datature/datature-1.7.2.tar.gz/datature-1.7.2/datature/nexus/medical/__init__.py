#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
  ████
██    ██   Datature
  ██  ██   Powering Breakthrough AI
    ██

@File    :   __init__.py
@Author  :   Raighne.Weng
@Version :   1.7.2
@Contact :   developers@datature.io
@License :   Apache License 2.0
@Desc    :   Processor package
"""

import pathlib
from os import PathLike

from .dicom_processor import DicomProcessor
from .nii_processor import NiiProcessor


def get_processor(file_path: PathLike):
    """Get processor"""

    extension = pathlib.Path(file_path).suffix.upper()

    if extension == ".DCM":
        return DicomProcessor()
    if extension == ".NII":
        return NiiProcessor()

    raise NotImplementedError
