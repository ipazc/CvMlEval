#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.dataset.simple_adience_dataset import SimpleAdienceDataset

__author__ = 'Iván de Paz Centeno'


class AgeEstimationDatasetLoader(Loader):
    def __init__(self):

        # Define the available datasets here
        available_datasets = {
            'simple_adience': SimpleAdienceDataset
        }

        Loader.__init__(self, available_datasets)
