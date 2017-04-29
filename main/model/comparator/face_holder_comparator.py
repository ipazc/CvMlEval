#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.comparator.comparator import Comparator

__author__ = 'Iván de Paz Centeno'


class FaceHolderComparator(Comparator):
    def __init__(self):
        Comparator.__init__(self, "face holder comparator", 1)

    def compare_images(self, image_original, image_processed):
        """
        Compares two images in order to determine if both images holds faces or not.

        :param image_original:
        :param image_processed:
        :return:    Returns 4 elements:

                        - The number of true positives.

                        - The number of false positives.

                        - The number of false negatives.

                        - The number of true negatives.
        """
        image_original_metadata = image_original.get_metadata()
        image_processed_metadata = image_processed.get_metadata()

        # We need to determine the following values:
        #
        #   number of true positives: 1 if both had faces; 0 otherwise.
        #   number of false positives: 1 if the processed image has faces but not the original. 0 Otherwise
        # image.
        #   number of false negatives: 1 if the processed image does not have faces but the original does.
        #   number of true negatives: 1 if both didn't have faces, 0 otherwise.

        original_image_has_faces = image_original_metadata[0]
        processed_image_has_faces = len(image_processed_metadata) > 0

        true_positives = int(original_image_has_faces and processed_image_has_faces)
        false_positives = int(not original_image_has_faces and processed_image_has_faces)
        false_negatives = int(original_image_has_faces and not processed_image_has_faces)
        true_negatives = int(not original_image_has_faces and not processed_image_has_faces)

        return true_positives, false_positives, false_negatives, true_negatives
