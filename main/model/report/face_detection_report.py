#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.report.report import Report

__author__ = 'Iván de Paz Centeno'


class FaceDetectionReport(Report):
    def __init__(self, description, algorithm, dataset):
        Report.__init__(self, description, algorithm, dataset)
        self.csv_lines += "image_id, total_faces_in_image, total_detected_faces_in_image, time_spent, true_positives, false_positives, false_negatives"
        self.total_faces = 0
        self.total_detected_faces = 0

    def add_result(self, image_id, total_faces_in_image, total_detected_faces_in_image, time_spent, true_positives,
                   false_positives, false_negatives):
        self.__anotate_line__(time_spent, true_positives, false_positives, false_negatives)
        self.total_faces += total_faces_in_image
        self.total_detected_faces += total_detected_faces_in_image
        self.csv_lines += "\n{}, {}, {}, {}, {}, {}, {}".format(image_id, total_faces_in_image,
                                                                total_detected_faces_in_image,
                                                                time_spent, true_positives,
                                                                false_positives, false_negatives)

    def __get_overall_info(self):
        overall = Report.__get_overall_info__(self)
        overall += "Total faces in dataset: {}\n".format(self.total_faces)
        overall += "Accuracy: {}%\n".format(round(self.total_true_positives / (self.total_true_positives + self.total_false_positives + self.total_false_negatives) * 100, 2))
        overall += "True positive rate: {}%\n".format(round(self.total_true_positives / (self.total_false_negatives + self.total_true_positives) * 100, 2))
        overall += "False positive rate: {}%\n".format(round(self.total_false_positives / (self.total_detected_faces) * 100, 2))
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