#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.metrics.confusionmatrix.confusion_matrix import ConfusionMatrix
from src.report.report import Report

__author__ = 'Iván de Paz Centeno'


class SkinDetectionReport(Report):
    def __init__(self, description, algorithm, dataset, threshold, extra):
        Report.__init__(self, description, algorithm, dataset)
        self.threshold = threshold
        self.threshold_description = extra
        self.csv_lines += "image_id, total_skin_in_image_pixels, total_detected_skin_pixels, time_spent, true_positive, false_positive, false_negative, true_negative, accuracy, recall, precision, fallout, miss_rate, f1_score, dices_coefficient, success"
        self.total_images = 0
        self.total_images_with_skin = 0
        self.total_successfully_detected_skin_images = 0
        self.total_true_negatives = 0
        self.total_precision_in_skin = 0
        self.total_recall_in_skin = 0
        self.total_f1_score_in_skin = 0
        self.total_dices_coefficient_in_skin = 0
        self.total_accuracy_in_no_skin = 0

    def add_result(self, image_id, total_skin_in_image_in_pixels, total_detected_skin_in_image_in_pixels, time_spent,
                   dices_coefficient, true_positive, false_positive, false_negative, true_negative, accuracy,
                   recall, precision, fallout, miss_rate, f1_score, success):

        self.__anotate_line__(time_spent, true_positive, false_positive, false_negative)
        self.total_true_negatives += true_negative

        self.total_images += 1

        if total_skin_in_image_in_pixels > 0:
            self.total_precision_in_skin += precision
            self.total_recall_in_skin += recall
            self.total_f1_score_in_skin += f1_score
            self.total_dices_coefficient_in_skin += dices_coefficient
            self.total_images_with_skin += 1
        else:
            self.total_accuracy_in_no_skin += accuracy

        if success:
            self.total_successfully_detected_skin_images += 1

        self.csv_lines += "\n{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(image_id, total_skin_in_image_in_pixels,
                                                                            total_detected_skin_in_image_in_pixels,
                                                                            time_spent, true_positive,
                                                                            false_positive, false_negative, true_negative,
                                                                            accuracy, recall, precision, fallout, miss_rate,
                                                                            f1_score, dices_coefficient, success)

    def __get_overall_info(self):
        overall = Report.__get_overall_info__(self)
        overall += "Total true negatives: {}\n".format(self.total_true_negatives)

        #overall += "Total true negatives: {}\n".format(self.total_true_negatives)
        overall += "Total skin images in dataset: {}\n".format(self.total_images)
        #overall += "Total successfully detected skin images: {}\n".format(self.total_successfully_detected_skin_images)

        """confusion_matrix = ConfusionMatrix.from_values(self.total_true_positives,
                                                       self.total_false_positives,
                                                       self.total_false_negatives,
                                                       self.total_true_negatives)
        """""
        #overall += confusion_matrix.get_report()

        if self.total_images_with_skin > 0:
            overall += "[SKIN] Global computed precision: {}%\n".format(
                round(self.total_precision_in_skin / self.total_images_with_skin, 2))
            overall += "[SKIN] Global computed recall: {}%\n".format(
                round(self.total_recall_in_skin / self.total_images_with_skin, 2))
            overall += "[SKIN] Global computed f1-score: {}\n".format(
                round(self.total_f1_score_in_skin / self.total_images_with_skin, 4))
            overall += "[SKIN] Global Dice's Coefficient: {}\n".format(
                round(self.total_dices_coefficient_in_skin / self.total_images_with_skin, 4))

        if self.total_images - self.total_images_with_skin > 0:
            overall += "[NO-SKIN] Global computed accuracy: {}\n".format(round(self.total_accuracy_in_no_skin / (self.total_images - self.total_images_with_skin), 2))

        return overall

    def __get_header__(self):
        header = Report.__get_header__(self)
        header += "Threshold: {}\n".format(self.threshold)
        header += "Threshold description: {}\n".format(self.threshold_description)
        return header

    def save_report(self, filename):
        self.__append__(self.__get_header__())
        self.__append__(self.__get_software_info__())
        self.__append__(self.__get_hardware_info__())
        self.__append__(self.__get_overall_info())
        self.__append__(self.csv_lines)
        Report.save_report(self, filename)