#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.facedetection.boundingbox.boundingbox import BoundingBox
from src.comparator.face_boundingbox_comparator import FaceBoundingBoxComparator
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'

import unittest


class FaceBoundingBoxComparatorTest(unittest.TestCase):

    def setUp(self):
        self.comparison_threshold = 0.9  # 90% of bounding boxes area must match
        self.comparator = FaceBoundingBoxComparator(self.comparison_threshold)

    def test_image_compare(self):
        image1_metadata = [BoundingBox(940, 219, 186, 185),
                          BoundingBox(1533, 493, 268, 268),
                          BoundingBox(485, 485, 223, 223)]
        image1 = Image("samples/image1.jpg", metadata=image1_metadata)

        image2_metadata = [BoundingBox(467, 505, 223, 223),
                           BoundingBox(945, 223, 181, 197),
                           BoundingBox(1589, 517, 233, 225)]
        image2 = Image("samples/image1.jpg", metadata=image2_metadata)

        # The comparator only parses the image metadata, so the URI is not needed at all

        intersections, true_positives, false_positives, false_negatives = self.comparator.compare_images(image1, image2)

        self.assertEqual(true_positives, 2)
        self.assertEqual(false_positives, 1)
        self.assertEqual(false_negatives, 1)

        expected_results = [[BoundingBox(945, 223, 181, 181), 0.9521, True],
                            [BoundingBox(1589, 517, 212, 225), 0.9099, True],
                            [BoundingBox(485, 505, 205, 203), 0.8368, False]]

        for boundingbox, intersection_percentage, threshold_reached in intersections:

            matches = False
            for expected_result in expected_results:

                if boundingbox.get_box() == expected_result[0].get_box() \
                        and intersection_percentage == expected_result[1] \
                        and threshold_reached == expected_result[2]:
                    matches = True

            self.assertTrue(matches)


if __name__ == '__main__':
    unittest.main()
