#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Iván de Paz Centeno'

# In src.algorithm.genderestimation we may have every gender estimation algorithm available to work with.

import sys

from src.algorithm.genderestimation.cnn_levi_hassner_gender_estimation_algorithm import \
    CNNLeviHassnerGenderEstimationAlgorithm
from src.resource.image.image import Image

gender_estimation_algorithm = CNNLeviHassnerGenderEstimationAlgorithm()


def get_usage():
    return "Usage:  python3 -m examples.gender_estimation_cnn_levi_hassner file.{png, jpg, jpeg, tiff}\n"


if len(sys.argv) == 1:
    print(get_usage())
    exit()

file = sys.argv[1]

image_result, time_spent = gender_estimation_algorithm.process_resource(Image(file))

# The image_result is an Image object with Gender associated (metadata).
if len(image_result.get_metadata()) == 0:
    print("No Gender estimated.")

for gender in image_result.get_metadata():
    print("Detected gender: {}".format(gender))

print("Process finished in {} seconds".format(time_spent))
