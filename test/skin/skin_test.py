#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.algorithm.skindetection.skin.skin import Skin
from src.metrics.confusionmatrix.skin_confusion_matrix import SkinConfusionMatrix
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'


class SkinTest(unittest.TestCase):

    def setUp(self):
        self.images =[[Image("samples/our-familly1.png"), Image("samples/our-familly2.png"), 19655],
                      [Image("samples/our-familly1.png"), Image("samples/our-familly1.png"), 41353],
                      [Image("samples/our-asdafamilly2.png"), Image("samples/our-familly1.png"), 0]]

        self.skin_image_to_compare_with = [
                            [Image("samples/skin_image_black.jpg"), 69.92, 0, 0.0],
                            [Image("samples/skin_image_white.jpg"), 30.08, 30.08, 100.0],
                            [Image("samples/our-familly_test1.png"), 99.0, 96.77, 100.0],
                            [Image("samples/our-familly_test2.png"), 99.0, 100.0, 96.67]
        ]

        self.skin_ground_truth_image = Image("samples/our-familly1.png")
        self.skin_ground_truth_image.load_from_uri(True)

    def testSkinIntersectionAndArea(self):
        for image_group in self.images:
            image1 = image_group[0]
            image2 = image_group[1]

            expected_area = image_group[2]

            skin1 = Skin(image1)
            skin2 = Skin(image2)

            self.assertEqual(skin1.intersect_with(skin2).get_area(), expected_area)

    def testSkinInvertAndComparison(self):

        ground_truth_skin = Skin(self.skin_ground_truth_image)

        for [image, accuracy, precision, recall] in self.skin_image_to_compare_with:
            image.load_from_uri(True)
            skin_to_compare = Skin(image)

            confusion_matrix = SkinConfusionMatrix(ground_truth_skin, skin_to_compare)
            self.assertEqual(confusion_matrix.get_accuracy(), accuracy)
            self.assertEqual(confusion_matrix.get_precision(), precision)
            self.assertEqual(confusion_matrix.get_recall(), recall)


if __name__ == '__main__':
    unittest.main()
