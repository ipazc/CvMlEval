#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.dataset.afw_dataset import AFWDataset

__author__ = 'Iván de Paz Centeno'


class FaceDetectionDatasetLoader(Loader):
    def __init__(self):

        # Define the available datasets here
        available_datasets = {
            'AFW': AFWDataset
        }

        Loader.__init__(self, available_datasets)
