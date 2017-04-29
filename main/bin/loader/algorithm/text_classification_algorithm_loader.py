#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.algorithm.textclassification.bow_logistic_regression_text_classification_algorithm import \
    BowLogisticRegressionTextClassificationAlgorithm
from src.algorithm.textclassification.bow_naive_bayes_text_classification_algorithm import \
    BowNaiveBayesTextClassificationAlgorithm
from src.algorithm.textclassification.bow_support_vector_machine_text_classification_algorithm import \
    BowSVMTextClassificationAlgorithm
from src.algorithm.textclassification.hashing_logistic_regression_text_classification_algorithm import \
    HashingLogisticRegressionTextClassificationAlgorithm
from src.algorithm.textclassification.hashing_support_vector_machine_text_classification_algorithm import \
    HashingSVMTextClassificationAlgorithm
from src.algorithm.textclassification.tfidf_logistic_regression_text_classification_algorithm import \
    TFIDFLogisticRegressionTextClassificationAlgorithm
from src.algorithm.textclassification.tfidf_naive_bayes_text_classification_algorithm import \
    TFIDFNaiveBayesTextClassificationAlgorithm
from src.algorithm.textclassification.tfidf_support_vector_machine_text_classification_algorithm import \
    TFIDFSVMTextClassificationAlgorithm

__author__ = 'Iván de Paz Centeno'


class TextClassificationAlgorithmLoader(Loader):
    def __init__(self):

        # Define the available algorithms here
        available_algorithms = {
            'bow_logistic_regression': BowLogisticRegressionTextClassificationAlgorithm,
            'bow_naive_bayes': BowNaiveBayesTextClassificationAlgorithm,
            'bow_support_vector_machine': BowSVMTextClassificationAlgorithm,
            'hashing_logistic_regression': HashingLogisticRegressionTextClassificationAlgorithm,
            'hashing_support_vector_machine': HashingSVMTextClassificationAlgorithm,
            'tfidf_logistic_regression': TFIDFLogisticRegressionTextClassificationAlgorithm,
            'tfidf_naive_bayes': TFIDFNaiveBayesTextClassificationAlgorithm,
            'tfidf_support_vector_machine': TFIDFSVMTextClassificationAlgorithm,
        }

        Loader.__init__(self, available_algorithms)
