#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Iván de Paz Centeno'

import unittest

from src.algorithm.facedetection.boundingbox.boundingbox import BoundingBox
from src.algorithm.facedetection.boundingbox.intersection2 import bb_intersection


class BoundingBoxTest(unittest.TestCase):

    def setUp(self):
        #                   rect1              rect2                 area_intersection  percentage
        self.rect_sets = [[[80, 60, 250, 170], [200, 130, 200, 170], 13000,             38.24],
                          [[80, 60, 40, 170], [200, 130, 200, 170],  0,                 0.00]]

    def test_intersection_with_boundingbox_class(self):
        for rect_set in self.rect_sets:
            rect1 = rect_set[0]
            rect2 = rect_set[1]
            expectedArea = rect_set[2]
            expectedPercentage = rect_set[3]

            box1 = BoundingBox(*rect1)
            box2 = BoundingBox(*rect2)

            intersection = box1.intersect_with(box2)
            number_of_common_pixels = intersection.get_area()

            # Which one is the smaller rectangle?
            area_box1 = box1.get_area()
            area_box2 = box2.get_area()

            lesser_area = min(area_box1, area_box2)
            percentage = round((number_of_common_pixels / lesser_area) * 100, 2)

            self.assertEqual(number_of_common_pixels, expectedArea)
            self.assertEqual(percentage, expectedPercentage)

    def test_intersection_with_pythonic_intersection2(self):
        for rect_set in self.rect_sets:
            rect1 = rect_set[0]
            rect2 = rect_set[1]
            expectedArea = rect_set[2]
            expectedPercentage = rect_set[3]

            [number_of_common_pixels, percentage] = bb_intersection(rect1, rect2)
            percentage = round(percentage * 100, 2)

            self.assertEqual(number_of_common_pixels, expectedArea)
            self.assertEqual(percentage, expectedPercentage)

    def test_expand(self):
        box1 = BoundingBox(3,3,100,100)
        box1.expand() # expand a default of 20%
        self.assertEqual(box1.get_box(), [-7,-7,120,120])   # If you see something weird here,
                                                            # remember that it is the width and height and not coords

    def test_expand_and_fit_in_size(self):
        image_size = [300, 300]

        # Case1 all out of bounds
        box1 = BoundingBox(-1, -1, 302, 302)
        box1.fit_in_size(image_size)
        self.assertEqual(box1.get_box(), [0, 0, 300, 300])

        # Case2 top left out of bounds
        box1 = BoundingBox(-1,-1,301,301)
        box1.fit_in_size(image_size)
        self.assertEqual(box1.get_box(), [0, 0, 300, 300])

        # Case left out of bounds
        box1 = BoundingBox(-15, 10, 100, 100)
        box1.fit_in_size(image_size)
        self.assertEqual(box1.get_box(), [0, 10, 85, 100])

        # Case top out of bounds
        box1 = BoundingBox(15, -10, 100, 100)
        box1.fit_in_size(image_size)
        self.assertEqual(box1.get_box(), [15, 0, 100, 90])

        # Case width out of bounds
        box1 = BoundingBox(15, 0, 290, 100)
        box1.fit_in_size(image_size)
        self.assertEqual(box1.get_box(), [15, 0, 285, 100])

        # Case height out of bounds
        box1 = BoundingBox(15, 15, 200, 290)
        box1.fit_in_size(image_size)
        self.assertEqual(box1.get_box(), [15, 15, 200, 285])


if __name__ == '__main__':
    unittest.main()
