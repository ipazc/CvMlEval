#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bin.loader.loader import Loader
from src.algorithm.facedetection.dlib_face_detection_algorithm import DLibFaceDetectionAlgorithm
from src.algorithm.facedetection.neven_face_detection_algorithm import NevenFaceDetectionAlgorithm
from src.algorithm.facedetection.opencv_face_detection_algorithm import OpenCVFaceDetectionAlgorithm

__author__ = 'Iván de Paz Centeno'


class FaceDetectionAlgorithmLoader(Loader):
    def __init__(self):

        # Define the available algorithms here
        available_algorithms = {
            'face_detection_dlib': DLibFaceDetectionAlgorithm,
            'face_detection_opencv': OpenCVFaceDetectionAlgorithm,
            'face_detection_neven': NevenFaceDetectionAlgorithm
        }

        Loader.__init__(self, available_algorithms)
