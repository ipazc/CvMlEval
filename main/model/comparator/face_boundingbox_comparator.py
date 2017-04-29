#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.comparator.comparator import Comparator

__author__ = 'Iván de Paz Centeno'


class FaceBoundingBoxComparator(Comparator):
    def __init__(self, match_threshold):
        Comparator.__init__(self, "Bounding boxes of faces comparator", match_threshold)

    def __find_matches(self, bounding_boxes1, bounding_boxes2):

        matches = {}
        intersections = []

        for boundingbox1 in bounding_boxes1:

            for boundingbox2 in bounding_boxes2:

                subiteration_matches = False

                intersection_box = boundingbox1.intersect_with(boundingbox2)

                smallest_area = min(boundingbox1.get_area(), boundingbox2.get_area())
                intersection_percentage = round(intersection_box.get_area() / smallest_area, 4)

                if intersection_percentage >= self.comparison_threshold:
                    matches[boundingbox1] = boundingbox2
                    subiteration_matches = True

                if intersection_percentage > 0:
                    intersections.append([intersection_box, intersection_percentage, subiteration_matches])

        return matches, intersections

    def compare_images(self, image_original, image_processed):
        """
        Compares two images in order to determine if the bounding boxes related to a face detection matches in both
        images or not.
        In order for them to match, a threshold (given during the construction of the object) must be reached for each
        bounding box.

        :param image_original:
        :param image_processed:
        :return:    Returns 4 elements:

                        - a list of intersections. Holds all the intersection bounding boxes associated with the
                        percentage of intersection with the lesser bounding box and if the threshold is over-passed or
                        not. It is a list with 3 components:
                        [ bounding box, percentage of intersection, threshold reached ].

                        - The number of matches.

                        - The number of false positives

                        - The number of false negatives
        """
        image_original_metadata = image_original.get_metadata()
        image_processed_metadata = image_processed.get_metadata()

        # We need to determine the following values:
        #
        #   number of true positives: the bounding boxes from the processed image that matches the original image.
        #   number of false positives: the bounding boxes from the processed image that does not match the original
        # image.
        #   number of false negatives: the bounding boxes from the original image that does not have any match.

        matches, intersections = self.__find_matches(image_processed_metadata, image_original_metadata)
        matches_inverted = dict((v,k) for k,v in matches.items())

        # matches is a dictionary of the form BoundingBox => BoundingBox.
        # If we invert the dictionary, we may have less keys than before. This means that the key is repeated,
        # thus something went wrong -> multiple detection for the same label.

        true_positives = len(matches_inverted)
        false_positives = abs(len(image_processed_metadata) - true_positives)
        false_negatives = abs(len(image_original_metadata) - true_positives)

        return intersections, true_positives, false_positives, false_negatives
