#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.comparator.comparator import Comparator

__author__ = 'Iván de Paz Centeno'


class GenderComparator(Comparator):

    def __init__(self):
        Comparator.__init__(self, "Gender comparator", 1)

    def __find_matches(self, genders1, genders2):

        matches = {}
        intersections = []

        for gender1 in genders1:

            for gender2 in genders2:

                subiteration_matches = False

                if gender1.get_gender() == gender2.get_gender():
                    intersection_percentage = 1
                else:
                    intersection_percentage = 0

                if intersection_percentage >= self.comparison_threshold:
                    matches[gender1] = gender2
                    subiteration_matches = True

                if intersection_percentage > 0:
                    intersections.append([gender1, intersection_percentage, subiteration_matches])

        return matches, intersections

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
                        [ gender, percentage of intersection, threshold reached ].

                        - The number of true positives.

                        - The number of false positives

                        - The number of false negatives
        """
        image_original_metadata = image_original.get_metadata()
        image_processed_metadata = image_processed.get_metadata()

        # We need to determine the following values:
        #
        #   number of true positives: the age ranges from the processed image that matches the original image.
        #   number of false positives: the age ranges from the processed image that does not match the original
        # image.
        #   number of false negatives: the age ranges from the original image that does not have any match.

        matches, intersections = self.__find_matches(image_processed_metadata, image_original_metadata)
        matches_inverted = dict((v, k) for k, v in matches.items())

        # matches is a dictionary of the form AgeRange => AgeRange.
        # If we invert the dictionary, we may have less keys than before. This means that the key is repeated,
        # thus something went wrong -> multiple detection for the same label.

        true_positives = len(matches_inverted)
        false_positives = abs(len(image_processed_metadata) - true_positives)
        false_negatives = abs(len(image_original_metadata) - true_positives)

        return intersections, true_positives, false_positives, false_negatives
