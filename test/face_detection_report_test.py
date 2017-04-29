#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.report.face_detection_report import FaceDetectionReport

__author__ = 'Iván de Paz Centeno'

import unittest


class FaceDetectionReportTest(unittest.TestCase):

    def setUp(self):
        self.report = FaceDetectionReport("Report for face detection", "test", "test")

    def test_save_report(self):
        self.report.add_result(123, 22, 1, 2, 1, 0, 1)
        self.report.add_result(123, 22, 1, 2, 1, 0, 1)
        self.report.add_result(123, 22, 1, 2, 1, 0, 1)
        self.report.add_result(123, 22, 1, 2, 1, 0, 1)
        self.report.add_result(123, 22, 1, 2, 1, 0, 1)
        self.report.add_result(123, 22, 1, 2, 1, 0, 1)

        self.report.save_report('samples/report.txt')

if __name__ == '__main__':
    unittest.main()
