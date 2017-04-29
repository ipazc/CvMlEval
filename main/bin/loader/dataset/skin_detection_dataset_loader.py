#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.dataset.pratheepan_dataset import PratheepanDataset

__author__ = 'Iván de Paz Centeno'


class SkinDetectionDatasetLoader(Loader):
    def __init__(self):

        # Define the available datasets here
        available_datasets = {
            'pratheepan': PratheepanDataset
        }

        Loader.__init__(self, available_datasets)
