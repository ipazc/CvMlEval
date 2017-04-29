#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.ageestimation.agerange.age_range import AgeRange

__author__ = 'Iván de Paz Centeno'

import unittest


class AgeRangeTest(unittest.TestCase):

    def setUp(self):
        #                   age1     age2     distance_intersection  percentage
        self.age_sets = [[[1, 30], [25, 60], 5,                     17.24],
                         [[5, 10], [30,60],  0,                     0.00]]

    def test_intersection_with_age_range_class(self):
        for age_set in self.age_sets:
            age1 = age_set[0]
            age2 = age_set[1]
            expected_distance = age_set[2]
            expected_percentage = age_set[3]

            age_range1 = AgeRange(*age1)
            age_range2 = AgeRange(*age2)

            intersection = age_range1.intersect_with(age_range2)
            intersection_distance = intersection.get_distance()

            # Which one is the smaller rectangle?
            distance_age1 = age_range1.get_distance()
            distance_age2 = age_range2.get_distance()

            lesser_distance = min(distance_age1, distance_age2)
            percentage = round((intersection_distance / lesser_distance) * 100, 2)

            self.assertEqual(intersection_distance, expected_distance)
            self.assertEqual(percentage, expected_percentage)


if __name__ == '__main__':
    unittest.main()
