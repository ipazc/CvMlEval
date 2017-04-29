#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
from numpy.distutils import cpuinfo
import time
import sys

__author__ = 'Iván de Paz Centeno'


class Report(object):
    def __init__(self, description, algorithm, dataset):
        self.total_time_spent = 0
        self.total_true_positives = 0
        self.total_false_positives = 0
        self.total_false_negatives = 0
        self.description = description
        self.algorithm = algorithm
        self.dataset = dataset
        self.text = ""
        self.lines_count = 0
        self.csv_lines = "\n==============================================\n" \
                         "CSV LINES\n" \
                         "==============================================\n"

    def __get_header__(self):
        return "==============================================\n" \
               "REPORT BUILT FOR {}\n" \
               "==============================================\n" \
               "Algorithm: {}\n" \
               "Dataset: {}\n" \
               "Dataset files count: {}\n" \
               "Date: {}\n".format(self.description, self.algorithm, self.dataset,
                                   self.lines_count, time.strftime("%c"))

    def __get_hardware_info__(self):
        with open('/proc/meminfo') as meminfo_file:
            meminfo = meminfo_file.readlines()

        meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in meminfo)
        mem_total_kib = meminfo['MemTotal']  # e.g. 3921852

        return "\n==============================================\n" \
               "HARDWARE INFO\n" \
               "==============================================\n" \
               "CPU model: {}\n" \
               "CPU cores: {}\n" \
               "CPU core threads: {}\n" \
               "RAM memory: {} GiB \n".format(cpuinfo.cpu.info[0]['model name'],
                                              cpuinfo.cpu.info[0]['cpu cores'],
                                              cpuinfo.cpu.info[0]['siblings'],
                                              round(mem_total_kib / 1014 / 1024, 2))

    def __get_software_info__(self):
        return "\n==============================================\n" \
               "SOFTWARE INFO\n" \
               "==============================================\n" \
               "Platform: {}\n" \
               "Python version: {}\n".format(platform.platform(), sys.version)

    def __anotate_line__(self, time_spent, true_positives, false_positives, false_negatives):
        self.total_time_spent += time_spent
        self.total_true_positives += true_positives
        self.total_false_positives += false_positives
        self.total_false_negatives += false_negatives
        self.lines_count += 1

    def __get_overall_info__(self):
        m, s = divmod(self.total_time_spent, 60)
        h, m = divmod(m, 60)

        return "\n==============================================\n" \
               "OVERALL INFO\n" \
               "==============================================\n" \
               "Total time spent: {} seconds ({} hours, {} minutes and {} seconds)\n" \
               "Total true positives: {}\n" \
               "Total false positives: {}\n" \
               "Total false negatives: {}\n".format(round(self.total_time_spent, 2), round(h), round(m), round(s, 2),
                                                    self.total_true_positives,
                                                    self.total_false_positives, self.total_false_negatives)

    def __append__(self, text):
        self.text += text

    def save_report(self, filename):

        with open(filename, "w") as text_file:
            print(self.text, file=text_file)
