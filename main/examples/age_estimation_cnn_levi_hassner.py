#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Iván de Paz Centeno'

# In src.algorithm.ageestimation we may have every age estimation algorithm available to work with.

import sys

from src.algorithm.ageestimation.cnn_levi_hassner_age_estimation_algorithm import CNNLeviHassnerAgeEstimationAlgorithm
from src.resource.image.image import Image

age_estimation_algorithm = CNNLeviHassnerAgeEstimationAlgorithm()


def get_usage():
    return "Usage:  python3 -m examples.age_estimation_cnn_levi_hassner file.{png, jpg, jpeg, tiff}\n"


if len(sys.argv) == 1:
    print(get_usage())
    exit()

file = sys.argv[1]

image_result, time_spent = age_estimation_algorithm.process_resource(Image(file))

# The image_result is an Image object with AgeRange associated (metadata).
if len(image_result.get_metadata()) == 0:
    print("No Ages estimated.")

for age_range in image_result.get_metadata():
    print("Detected age range: {}".format(age_range))

print("Process finished in {} seconds".format(time_spent))
