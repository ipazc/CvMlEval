#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.metrics.confusionmatrix.confusion_matrix import ConfusionMatrix

__author__ = 'Ivan de Paz Centeno'


class SkinConfusionMatrix(ConfusionMatrix):

    def __init__(self, skin_ground_truth, skin_to_compute):
        ConfusionMatrix.__init__(self)

        skin_inverted_ground_truth = skin_ground_truth.get_inverted()
        skin_inverted_to_compute = skin_to_compute.get_inverted()

        skin_intersection = skin_to_compute.intersect_with(skin_ground_truth)
        skin_inverted_intersection = skin_inverted_to_compute.intersect_with(skin_inverted_ground_truth)

        self.true_positives = skin_intersection.get_area()
        self.false_positives = skin_to_compute.get_area() - self.true_positives
        self.true_negatives = skin_inverted_intersection.get_area()
        self.false_negatives = skin_inverted_to_compute.get_area() - self.true_negatives
