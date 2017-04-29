#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.ageestimation.agerange.age_range import AgeRange
from src.comparator.age_range_comparator import AgeRangeComparator
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'

import unittest


class AgeRangeComparatorTest(unittest.TestCase):

    def setUp(self):
        self.comparison_threshold = 0.9  # 90% of age ranges area must match
        self.comparator = AgeRangeComparator(self.comparison_threshold)

    def test_image_compare(self):
        image1_metadata = [AgeRange(25, 32),
                           AgeRange(0, 2),
                           AgeRange(10, 30),
                           AgeRange(50, 60)]
        image1 = Image(uri="samples/image1.jpg", metadata=image1_metadata)

        image2_metadata = [AgeRange(30, 40),
                           AgeRange(1, 1),
                           AgeRange(10, 15),
                           AgeRange(-1, -1)]
        image2 = Image(uri="samples/image1.jpg", metadata=image2_metadata)

        # The comparator only parses the image metadata, so the URI is not needed at all

        intersections, true_positives, false_positives, false_negatives = self.comparator.compare_images(image1, image2)

        self.assertEqual(true_positives, 1)
        self.assertEqual(false_positives, 3)
        self.assertEqual(false_negatives, 3)

        expected_results = [[AgeRange(30, 32), 0.2857, False],
                            [AgeRange(10, 15), 1.0, True]]

        for age_range, intersection_percentage, threshold_reached in intersections:

            matches = False
            for expected_result in expected_results:
                if age_range.get_range() == expected_result[0].get_range() \
                        and intersection_percentage == expected_result[1] \
                        and threshold_reached == expected_result[2]:
                    matches = True

            self.assertTrue(matches)


if __name__ == '__main__':
    unittest.main()
