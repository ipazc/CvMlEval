#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ivan de Paz Centeno'


class SkinSorensenDiceMetric(object):

    def __init__(self, skin_original, skin_processed, confusion_matrix):
        self.skin_original_area = skin_original.get_area()
        self.skin_processed_area = skin_processed.get_area()
        self.confusion_matrix = confusion_matrix

    def get_metric_value(self, as_percentage=True):

        total_area = (self.skin_original_area + self.skin_processed_area)

        if total_area == 0:
            value = 0
        else:
            value = 2 * self.confusion_matrix.get_true_positives() / total_area

        if as_percentage:
            value = round(value* 100, 2)

        return value
