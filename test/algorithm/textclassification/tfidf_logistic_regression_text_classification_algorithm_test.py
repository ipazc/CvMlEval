#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.algorithm.textclassification.tfidf_logistic_regression_text_classification_algorithm import \
    TFIDFLogisticRegressionTextClassificationAlgorithm
from src.resource.text.text import Text

__author__ = 'Iván de Paz Centeno'


class TFIDFLogisticRegressionTextClassificationAlgorithmTest(unittest.TestCase):

    def setUp(self):

        self.algorithm = TFIDFLogisticRegressionTextClassificationAlgorithm()
        self.sample_text_to_process = [[Text("samples/OnionFiles/uhkplurmvltqen4k.onion.dump"), 'Counterfeit'],
                                       [Text("samples/OnionFiles/uksfvgmwpiww3n4s.onion.dump"), 'Firearms'],
                                       [Text("samples/OnionFiles/y3nau3mnibjbpmh4.onion.dump"), 'Pornography'],
                                       [Text("samples/OnionFiles/zce4p7bavtstnwzt.onion.dump"), 'Hacking']]

    def test_prediction(self):

        for text, truth_value in self.sample_text_to_process:
            text_result, time_spent = self.algorithm.process_resource(text)
            text_metadata = text_result.get_metadata()
            predicted_value = text_metadata[0]
            self.assertEqual(predicted_value, truth_value)


if __name__ == '__main__':
    unittest.main()
