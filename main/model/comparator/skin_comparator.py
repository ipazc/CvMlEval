#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.comparator.comparator import Comparator
from src.metrics.confusionmatrix.skin_confusion_matrix import SkinConfusionMatrix
from src.metrics.skin_sorensen_dice_metric import SkinSorensenDiceMetric

__author__ = 'Iván de Paz Centeno'


class SkinComparator(Comparator):

    def __init__(self, match_threshold):
        Comparator.__init__(self, "Skin comparator", match_threshold)

    def compare_images(self, image_original, image_processed):
        """
        Compares two images in order to determine if the skin associated to one matches with the skin
        associated with the other.
        In order for them to match, a threshold (given during the construction of the object) must be reached for the
        _dice's coefficient_ of the skin of the processed image compared to the original one.

        :param image_original:
        :param image_processed:
        :return:    Returns 5 elements:
                        - The confusion matrix

                        - Dice's coefficient
        """
        image_original_metadata = image_original.get_metadata()
        image_processed_metadata = image_processed.get_metadata()

        skin_processed = image_processed_metadata[0]
        skin_original = image_original_metadata[0]

        #threshold = round(self.get_threshold() * 100, 2)
        #TODO: Use a threshold to determine if the detection is successful or not.

        confusion_matrix = SkinConfusionMatrix(skin_original, skin_processed)
        skin_sorensen_dice_metric = SkinSorensenDiceMetric(skin_original, skin_processed, confusion_matrix)
        dice_coefficient = skin_sorensen_dice_metric.get_metric_value()

        return confusion_matrix, dice_coefficient
