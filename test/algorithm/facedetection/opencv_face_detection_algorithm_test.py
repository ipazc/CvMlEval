#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.facedetection.opencv_face_detection_algorithm import OpenCVFaceDetectionAlgorithm
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'

import unittest


class OpenCVFaceDetectionAlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.algorithm = OpenCVFaceDetectionAlgorithm()
        self.sampleImageToTest = Image("samples/image1.jpg")

        self.boundingbox_to_match = [[935, 181, 223, 223],
                                     [1530, 468, 272, 272],
                                     [468, 458, 263, 263]]

    def test_detection(self):
        image_result, time_spent = self.algorithm.process_resource(self.sampleImageToTest)
        image_metadata = image_result.get_metadata()

        self.assertGreater(time_spent, 0)
        self.assertEqual(len(image_metadata), len(self.boundingbox_to_match))

        for boundingbox in image_metadata:
            matches = False

            for bbox in self.boundingbox_to_match:
                matches = matches or (boundingbox.get_box() == bbox)

            self.assertTrue(matches)


if __name__ == '__main__':
    unittest.main()
