#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.algorithm.skindetection.bayes_lut_dempster_shafer_skin_detection_algorithm import \
    BayesLutDempsterShaferSkinDetectionAlgorithm
from src.algorithm.skindetection.skin.skin import Skin
from src.metrics.confusionmatrix.skin_confusion_matrix import SkinConfusionMatrix
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'


class BayesLutDempsterShaferSkinDetectionAlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.algorithm = BayesLutDempsterShaferSkinDetectionAlgorithm()
        self.sample_image_to_process = Image("samples/our-familly_original.jpg")
        self.sample_image_to_compare_with = [
            [Image("samples/our-familly1.png"), True],
            [Image("samples/skin_image_black.jpg"), True],
            [Image("samples/skin_image_white.jpg"), False]]

        self.accuracy_threshold = 46.0

    def test_detection(self):

        image_result, time_spent = self.algorithm.process_resource(self.sample_image_to_process)
        image_metadata = image_result.get_metadata()
        detected_skin = image_metadata[0]

        self.assertGreater(time_spent, 0)
        self.assertEqual(len(image_metadata), 1)

        for [ground_truth_image, matches] in self.sample_image_to_compare_with:
            ground_truth_image.load_from_uri(True)
            ground_truth_skin = Skin(ground_truth_image)

            confusion_matrix = SkinConfusionMatrix(ground_truth_skin, detected_skin)

            self.assertEqual(confusion_matrix.get_accuracy() > self.accuracy_threshold, matches)


if __name__ == '__main__':
    unittest.main()
