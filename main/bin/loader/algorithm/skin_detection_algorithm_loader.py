#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.algorithm.skindetection.bayes_lut_dempster_shafer_skin_detection_algorithm import \
    BayesLutDempsterShaferSkinDetectionAlgorithm
from src.algorithm.skindetection.bayes_lut_skin_detection_algorithm import BayesLutSkinDetectionAlgorithm
from src.algorithm.skindetection.chai_1999_skin_detection_algorithm import Chai1999SkinDetectionAlgorithm
from src.algorithm.skindetection.cheddad_2009_skin_detection_algorithm import Cheddad2009SkinDetectionAlgorithm
from src.algorithm.skindetection.gaussian_distributed_skin_detection_algorithm import \
    GaussianDistributedSkinDetectionAlgorithm
from src.algorithm.skindetection.hsieh_2002_skin_detection_algorithm import Hsieh2002SkinDetectionAlgorithm
from src.algorithm.skindetection.kovak_2003_fl_skin_detection_algorithm import Kovak2003FLSkinDetectionAlgorithm
from src.algorithm.skindetection.kovak_2003_ud_skin_detection_algorithm import Kovak2003UDSkinDetectionAlgorithm
from src.algorithm.skindetection.simple_color_threshold_skin_detection_algorithm import \
    SimpleColorThresholdSkinDetectionAlgorithm
from src.algorithm.skindetection.soriano_2000_skin_detection_algorithm import Soriano2000SkinDetectionAlgorithm

__author__ = 'Iván de Paz Centeno'


class SkinDetectionAlgorithmLoader(Loader):
    def __init__(self):

        # Define the available algorithms here
        available_algorithms = {
            'skin_detection_simple_color': SimpleColorThresholdSkinDetectionAlgorithm,
            'bayes_lut': BayesLutSkinDetectionAlgorithm,
            'bayes_lut_dempster_shafer': BayesLutDempsterShaferSkinDetectionAlgorithm,
            'chai_1999': Chai1999SkinDetectionAlgorithm,
            'cheddad_2009': Cheddad2009SkinDetectionAlgorithm,
            'gaussian_distributed': GaussianDistributedSkinDetectionAlgorithm,
            'hsieh_2002': Hsieh2002SkinDetectionAlgorithm,
            'kovak_2003_fl': Kovak2003FLSkinDetectionAlgorithm,
            'kovak_2003_ud': Kovak2003UDSkinDetectionAlgorithm,
            'soriano_2000': Soriano2000SkinDetectionAlgorithm,
        }

        Loader.__init__(self, available_algorithms)
