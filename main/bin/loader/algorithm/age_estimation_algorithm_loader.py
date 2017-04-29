#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.algorithm.ageestimation.cnn_levi_hassner_age_estimation_algorithm import CNNLeviHassnerAgeEstimationAlgorithm
from src.algorithm.ageestimation.cnn_rothe_apparent_age_estimation_algorithm import \
    CNNRotheApparentAgeEstimationAlgorithm
from src.algorithm.ageestimation.cnn_rothe_real_age_estimation_algorithm import CNNRotheRealAgeEstimationAlgorithm

__author__ = 'Iván de Paz Centeno'


class AgeEstimationAlgorithmLoader(Loader):
    def __init__(self):

        # Define the available algorithms here
        available_algorithms = {
            'age_estimation_cnn_levi_hassner': CNNLeviHassnerAgeEstimationAlgorithm,
            'age_estimation_rothe_real': CNNRotheRealAgeEstimationAlgorithm,
            'age_estimation_rothe_apparent': CNNRotheApparentAgeEstimationAlgorithm
        }

        Loader.__init__(self, available_algorithms)
