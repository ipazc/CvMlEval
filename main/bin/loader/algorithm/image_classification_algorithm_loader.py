#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.algorithm.imageclassification.bow_svm_image_classification_linear_kernel_algorithm import \
    BowSVMImageClassificationLinearKernelAlgorithm
from src.algorithm.imageclassification.bow_svm_image_classification_poly5_kernel_algorithm import \
    BowSVMImageClassificationPoly5KernelAlgorithm
from src.algorithm.imageclassification.bow_svm_image_classification_rbf_kernel_algorithm import \
    BowSVMImageClassificationRBFKernelAlgorithm

__author__ = 'Iván de Paz Centeno'


class ImageClassificationAlgorithmLoader(Loader):
    def __init__(self):

        # Define the available algorithms here
        available_algorithms = {
            'bow_svm_linear_kernel': BowSVMImageClassificationLinearKernelAlgorithm,
            'bow_svm_poly5_kernel': BowSVMImageClassificationPoly5KernelAlgorithm,
            'bow_svm_rbf_kernel': BowSVMImageClassificationRBFKernelAlgorithm
        }

        Loader.__init__(self, available_algorithms)
