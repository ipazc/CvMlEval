#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Iván de Paz Centeno'


class Comparator(object):

    def __init__(self, description, comparison_threshold):
        """

        :param description: the comparator full text description.
        :param comparison_threshold: a value that will be used as a threshold. Can be float or int.
        """
        self.description = description
        self.comparison_threshold = comparison_threshold

    def get_description(self):
        return self.description

    def compare_images(self, image1, image2):
        """
        Compares two images and returns information related to the comparison. Each algorithm will return different
        results.

        :param image1:  Image class filled. The information requested in the Image depends on the algorithms
        requirements.
        :param image2:  Image class filled. The information requested in the Image depends on the algorithms
        requirements.
        :return:
        """
        # TODO: implement this method for each comparator
        return []

    def __str__(self):
        return self.get_description()

    def get_threshold(self):
        return self.comparison_threshold
