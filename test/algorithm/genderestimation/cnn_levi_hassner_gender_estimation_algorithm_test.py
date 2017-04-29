#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.genderestimation.cnn_levi_hassner_gender_estimation_algorithm import \
    CNNLeviHassnerGenderEstimationAlgorithm
from src.algorithm.genderestimation.gender.gender import Gender, GENDER_FEMALE
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'

import unittest


class CNNLeviHassnerGenderEstimationAlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.algorithm = CNNLeviHassnerGenderEstimationAlgorithm()
        self.sampleImageToTest = Image("samples/example_image.jpg")

        self.gender_to_match = Gender(GENDER_FEMALE)

    def test_estimation(self):
        image_result, time_spent = self.algorithm.process_resource(self.sampleImageToTest)
        image_metadata = image_result.get_metadata()

        predicted_gender = image_metadata[0]

        self.assertGreater(time_spent, 0)
        self.assertEqual(predicted_gender.get_gender(), self.gender_to_match.get_gender())

if __name__ == '__main__':
    unittest.main()
