#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main.model.comparator.comparator import Comparator

__author__ = 'Iván de Paz Centeno'


class SingleAgeRangeComparator(Comparator):

    def __init__(self):
        Comparator.__init__(self, "Single age range comparator", 1)

    def __find_match(self, age_range1, age_range2):
        intersection = age_range1.intersect_with(age_range2)

        matches = intersection.get_mean() > -1

        return matches, intersection

    def compare_images(self, image_original, image_processed):
        """
        Compares two images in order to determine if the age_ranges associated to one matches with the age_ranges
        associated with the other.
        In order for them to match, a threshold (given during the construction of the object) must be reached for the
        intersection age range with each age_range.

        :param image_original:
        :param image_processed:
        :return:    Returns 4 elements:

                        - A list of intersections. Holds all the intersection age ranges associated with the
                        percentage of intersection with the lesser age_range and if the threshold is over-passed or
                        not. It is a list with 3 components:
                        [ age range, percentage of intersection, threshold reached ].

                        - The number of true positives.

                        - The number of false positives

                        - The number of false negatives
        """
        image_original_metadata = image_original.get_metadata()
        image_processed_metadata = image_processed.get_metadata()

        match, intersection = self.__find_match(image_processed_metadata[0], image_original_metadata[0])

        return intersection, int(match)
