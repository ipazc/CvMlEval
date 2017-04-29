#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.algorithm.imageclassification.bow_svm_image_classification_rbf_kernel_algorithm import \
    BowSVMImageClassificationRBFKernelAlgorithm
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'


class BowSVMImageClassificationRBFKernelAlgorithmTest(unittest.TestCase):

    def setUp(self):

        self.algorithm = BowSVMImageClassificationRBFKernelAlgorithm()
        self.sample_image_to_process = [[Image("samples/euro_note_060.jpg"), 'note'],
                                        [Image("samples/euro_note_060.jpg"), 'note'],
                                        [Image("samples/pistol_8.jpg"), 'note'],
                                        [Image("samples/pistol_25.jpg"), 'note'],
                                        [Image("samples/almost_naked_Bing_004.jpg"), 'almost_naked'],
                                        [Image("samples/almost_naked_Bing_063.jpg"), 'almost_naked'],
                                        [Image("samples/marihuana_Bing_006.jpg"), 'note'],
                                        [Image("samples/marihuana_Bing_011.jpg"), 'note']]

    def test_prediction(self):

        for image, truth_value in self.sample_image_to_process:
            image_result, time_spent = self.algorithm.process_resource(image)
            image_metadata = image_result.get_metadata()
            predicted_value = image_metadata[0]

            self.assertEqual(predicted_value, truth_value)


if __name__ == '__main__':
    unittest.main()
