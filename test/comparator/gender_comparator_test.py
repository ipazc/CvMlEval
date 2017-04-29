#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.genderestimation.gender.gender import Gender, GENDER_MALE, GENDER_FEMALE
from src.comparator.gender_comparator import GenderComparator
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'

import unittest


class GenderComparatorTest(unittest.TestCase):

    def setUp(self):
        self.comparator = GenderComparator()

    def test_image_compare(self):
        image1_metadata = [Gender(GENDER_MALE),
                           Gender(GENDER_FEMALE)]
        image1 = Image("samples/image1.jpg", metadata=image1_metadata)

        image2_metadata = [Gender(GENDER_FEMALE),
                           Gender(GENDER_FEMALE)]
        image2 = Image("samples/image1.jpg", metadata=image2_metadata)

        # The comparator only parses the image metadata, so the URI is not needed at all

        intersections, true_positives, false_positives, false_negatives = self.comparator.compare_images(image1, image2)

        self.assertEqual(true_positives, 1)
        self.assertEqual(false_positives, 1)
        self.assertEqual(false_negatives, 1)

        expected_results = [[Gender(GENDER_FEMALE), 1.0, True]]

        for gender, intersection_percentage, threshold_reached in intersections:

            matches = False
            for expected_result in expected_results:
                if gender.get_gender() == expected_result[0].get_gender() \
                        and intersection_percentage == expected_result[1] \
                        and threshold_reached == expected_result[2]:
                    matches = True

            self.assertTrue(matches)


if __name__ == '__main__':
    unittest.main()
