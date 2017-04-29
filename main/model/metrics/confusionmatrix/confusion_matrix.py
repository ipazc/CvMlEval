#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ivan de Paz Centeno'


class ConfusionMatrix(object):

    def __init__(self):
        self.true_positives = 0
        self.false_positives = 0
        self.true_negatives = 0
        self.false_negatives = 0

    @classmethod
    def from_values(cls, true_positives, false_positives, false_negatives, true_negatives):

        instance = cls()
        instance.true_positives = true_positives
        instance.false_positives = false_positives
        instance.false_negatives = false_negatives
        instance.true_negatives = true_negatives

        return instance

    def get_true_positives(self):
        return self.true_positives

    def get_false_positives(self):
        return self.false_positives

    def get_true_negatives(self):
        return self.true_negatives

    def get_false_negatives(self):
        return self.false_negatives

    def get_recall(self, as_percentage=True):

        if self.true_positives + self.false_negatives == 0:
            recall = 0
        else:
            recall = self.true_positives / (self.true_positives + self.false_negatives)

        if as_percentage:
            recall = round(recall * 100, 2)

        return recall

    def get_specifity(self, as_percentage=True):

        negatives = self.false_positives + self.true_negatives

        if negatives == 0:
            specifity = 0
        else:
            specifity = self.true_negatives / negatives

        if as_percentage:
            specifity = round(specifity * 100, 2)

        return specifity

    def get_precision(self, as_percentage=True):

        if self.true_positives + self.false_positives == 0:
            precision = 0
        else:
            precision = self.true_positives / (self.true_positives + self.false_positives)

        if as_percentage:
            precision = round(precision * 100, 2)

        return precision

    def get_negative_predictive_value(self, as_percentage=True):

        if self.true_negatives + self.false_positives == 0:
            negative_predictive_value = 0
        else:
            negative_predictive_value = self.true_negatives / (self.true_negatives + self.false_negatives)

        if as_percentage:
            negative_predictive_value = round(negative_predictive_value * 100, 2)

        return negative_predictive_value

    def get_fallout(self, as_percentage=True):

        fallout = 1 - self.get_specifity(False)

        if as_percentage:
            fallout = round(fallout * 100, 2)

        return fallout

    def get_false_discovery_rate(self, as_percentage=True):

        false_discovery_rate = 1 - self.get_precision(False)

        if as_percentage:
            false_discovery_rate = round(false_discovery_rate * 100, 2)

        return false_discovery_rate

    def get_miss_rate(self, as_percentage=True):

        positives = self.false_negatives + self.true_positives

        if positives == 0:
            miss_rate = 0
        else:
            miss_rate = self.false_negatives / positives

        if as_percentage:
            miss_rate = round(miss_rate * 100, 2)

        return miss_rate

    def get_accuracy(self, as_percentage=True):

        positives = self.false_negatives + self.true_positives
        negatives = self.false_positives + self.true_negatives

        if positives + negatives == 0:
            accuracy = 0
        else:
            accuracy = (self.true_positives + self.true_negatives) / (positives + negatives)

        if as_percentage:
            accuracy = round(accuracy * 100, 2)

        return accuracy

    def get_f1_score(self, as_percentage=False):

        precision = self.get_precision(False)
        recall = self.get_recall(False)

        if precision + recall == 0:
            f1_score = 0
        else:
            f1_score = round(2*(precision*recall) / (precision + recall), 4)

        if as_percentage:
            f1_score = round(f1_score * 100, 2)

        return f1_score

    def __str__(self):
        return "tp:{} tn:{} fp:{} fn:{} acc:{} prec:{} rec:{} f1score:{}".format(self.true_positives, self.true_negatives,
                                                                      self.false_positives, self.false_negatives,
                                                                      self.get_accuracy(), self.get_precision(),
                                                                      self.get_recall(), self.get_f1_score())

    def get_report(self, as_percentage=True):
        report = ""

        if as_percentage:
            extra = "%"
        else:
            extra = ""

        report += "recall: {}{}\n".format(self.get_recall(as_percentage), extra)
        report += "precision: {}{}\n".format(self.get_precision(as_percentage), extra)
        report += "fallout: {}{}\n".format(self.get_fallout(as_percentage), extra)
        report += "miss rate: {}{}\n".format(self.get_miss_rate(as_percentage), extra)

        report += "specifity: {}{}\n".format(self.get_specifity(as_percentage), extra)
        report += "negative predictive value: {}{}\n".format(self.get_negative_predictive_value(as_percentage), extra)
        report += "false discovery rate: {}{}\n".format(self.get_false_discovery_rate(as_percentage), extra)

        report += "F1 Score: {}\n".format(self.get_f1_score())

        return report
