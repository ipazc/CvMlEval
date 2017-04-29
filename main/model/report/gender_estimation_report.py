#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.report.report import Report

__author__ = 'Iván de Paz Centeno'


class GenderEstimationReport(Report):
    def __init__(self, description, algorithm, dataset):
        Report.__init__(self, description, algorithm, dataset)
        self.csv_lines += "image_id, original_age, detected_age, time_spent, true_positives, false_positives, " \
                          "false_negatives"
        self.total_images = 0

    def add_result(self, image_id, original_gender, detected_gender, time_spent, true_positives,
                   false_positives, false_negatives):
        self.__anotate_line__(time_spent, true_positives, false_positives, false_negatives)
        self.csv_lines += "\n{}, {}, {}, {}, {}, {}, {}".format(image_id, original_gender,
                                                                detected_gender,
                                                                time_spent, true_positives,
                                                                false_positives, false_negatives)
        self.total_images += 1

    def __get_overall_info(self):
        overall = Report.__get_overall_info__(self)
        overall += "Total images in dataset: {}\n".format(self.total_images)
        overall += "Accuracy: {}%\n".format(round(self.total_true_positives / (self.total_true_positives + self.total_false_positives + self.total_false_negatives) * 100, 2))
        overall += "True positive rate: {}%\n".format(round(self.total_true_positives / (self.total_false_negatives + self.total_true_positives) * 100, 2))
        overall += "False positive rate: {}%\n".format(round(self.total_false_positives / self.total_images * 100, 2))
        overall += "False negative rate: {}%\n".format(round(self.total_false_negatives / (self.total_false_negatives + self.total_true_positives) * 100, 2))
        overall += "Precision rate: {}%\n".format(round(self.total_true_positives / (self.total_false_positives + self.total_true_positives) * 100, 2))
        return overall

    def save_report(self, filename):
        self.__append__(self.__get_header__())
        self.__append__(self.__get_software_info__())
        self.__append__(self.__get_hardware_info__())
        self.__append__(self.__get_overall_info())
        self.__append__(self.csv_lines)
        Report.save_report(self, filename)
