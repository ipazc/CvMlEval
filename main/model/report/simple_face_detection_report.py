#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.report.report import Report

__author__ = 'Iván de Paz Centeno'


class SimpleFaceDetectionReport(Report):
    def __init__(self, description, algorithm, dataset):
        Report.__init__(self, description, algorithm, dataset)
        self.csv_lines += "image_id, has_faces, did_algorithm_detect_faces"
        self.total_true_negatives = 0

    def add_result(self, image_id, has_faces, did_algorithm_detect_faces, time_spent, true_positives,
                   false_positives, false_negatives, true_negatives):
        self.total_true_negatives += true_negatives
        self.__anotate_line__(time_spent, true_positives, false_positives, false_negatives)
        self.csv_lines += "\n{}, {}, {}".format(image_id, has_faces, did_algorithm_detect_faces)

    def __get_overall_info(self):
        overall = Report.__get_overall_info__(self)
        overall += "Total images processed: {}\n".format(self.lines_count)
        overall += "Accuracy: {}%\n".format(round((self.total_true_positives + self.total_true_negatives)/ (self.total_true_positives + self.total_false_positives + self.total_false_negatives + self.total_true_negatives) * 100, 2))
        overall += "True positive rate (Sensitivity): {}%\n".format(round(self.total_true_positives / (self.total_false_negatives + self.total_true_positives) * 100, 2))
        overall += "False positive rate: {}%\n".format(round(self.total_false_positives / (self.total_false_positives + self.total_true_negatives) * 100, 2))
        overall += "False negative rate (miss rate): {}%\n".format(round(self.total_false_negatives / (self.total_false_negatives + self.total_true_positives) * 100, 2))
        overall += "True negative rate: {}%\n".format(round(self.total_true_negatives / (self.total_false_negatives + self.total_true_negatives) * 100, 2))
        overall += "Positive predictive value (Precision rate): {}%\n".format(round(self.total_true_positives / (self.total_false_positives + self.total_true_positives) * 100, 2))
        overall += "Negative predictive value: {}%\n".format(round(self.total_true_negatives / (self.total_true_negatives+ self.total_false_negatives) * 100, 2))
        overall += "False discovery rate: {}%\n".format(round(self.total_false_positives / (self.total_false_positives + self.total_true_positives) * 100, 2))
        overall += "F1 Score: {}%\n".format(round((2 * self.total_true_positives) / (2*self.total_true_positives + self.total_false_positives + self.total_false_negatives) * 100, 2))

        return overall

    def save_report(self, filename):
        self.__append__(self.__get_header__())
        self.__append__(self.__get_software_info__())
        self.__append__(self.__get_hardware_info__())
        self.__append__(self.__get_overall_info())
        self.__append__(self.csv_lines)
        Report.save_report(self, filename)
