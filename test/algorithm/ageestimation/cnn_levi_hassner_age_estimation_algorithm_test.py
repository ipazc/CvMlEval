#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.ageestimation.agerange.age_range import AgeRange
from src.algorithm.ageestimation.cnn_levi_hassner_age_estimation_algorithm import CNNLeviHassnerAgeEstimationAlgorithm
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'

import unittest


class CNNLeviHassnerAgeEstimationAlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.algorithm = CNNLeviHassnerAgeEstimationAlgorithm()
        self.sampleImageToTest = Image("samples/example_image.jpg")

        self.age_to_match = AgeRange(0, 2)

    def test_estimation(self):
        image_result, time_spent = self.algorithm.process_resource(self.sampleImageToTest)
        image_metadata = image_result.get_metadata()

        predicted_age = image_metadata[0]

        self.assertGreater(time_spent, 0)
        self.assertEqual(predicted_age.get_range(), self.age_to_match.get_range())

if __name__ == '__main__':
    unittest.main()
