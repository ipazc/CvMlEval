#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.dataset.edu_dataset import EduDataset

__author__ = 'Iván de Paz Centeno'

"""
Datasets whose grounding truth only specifies if a given image has faces or not, not its position.
"""


class SimpleFaceDetectionDatasetLoader(Loader):
    def __init__(self):

        # Define the available datasets here
        available_datasets = {
            'EDU': EduDataset
        }

        Loader.__init__(self, available_datasets)
