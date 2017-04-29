#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Iván de Paz Centeno'

# In src.algorithm.facedetection we may have every face detection algorithm available to work with.

import sys

from src.algorithm.facedetection.dlib_face_detection_algorithm import DLibFaceDetectionAlgorithm
from src.resource.image.image import Image

faceDetectionAlgorithm = DLibFaceDetectionAlgorithm()


def get_usage():
    return "Usage:  python3 -m examples.face_detection_dlib file.jpg\n"


if len(sys.argv) == 1:
    print(get_usage())
    exit()

file = sys.argv[1]

image_result, time_spent = faceDetectionAlgorithm.process_resource(Image(file))

# The image_result is an Image object with boundingboxes associated (metadata).
if len(image_result.get_metadata()) == 0:
    print("No faces detected.")

for boundingbox in image_result.get_metadata():
    print("Detected face, bounding box is: {}".format(boundingbox.get_box()))

print("Process finished in {} seconds".format(time_spent))
