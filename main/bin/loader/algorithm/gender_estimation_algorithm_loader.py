#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.algorithm.genderestimation.cnn_levi_hassner_gender_estimation_algorithm import \
    CNNLeviHassnerGenderEstimationAlgorithm
from src.algorithm.genderestimation.cnn_rothe_gender_estimation_algorithm import CNNRotheGenderEstimationAlgorithm

__author__ = 'Iván de Paz Centeno'


class GenderEstimationAlgorithmLoader(Loader):
    def __init__(self):

        # Define the available algorithms here
        available_algorithms = {
            'gender_estimation_cnn_levi_hassner': CNNLeviHassnerGenderEstimationAlgorithm,
            'gender_estimation_cnn_rothe': CNNRotheGenderEstimationAlgorithm
        }

        Loader.__init__(self, available_algorithms)
