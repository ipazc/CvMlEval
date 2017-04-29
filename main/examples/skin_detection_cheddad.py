#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from src.algorithm.skindetection.cheddad_2009_skin_detection_algorithm import Cheddad2009SkinDetectionAlgorithm
from src.drawer.skin_drawer import SkinDrawer
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'

# In src.algorithm.skindetection we may have every skin detection algorithm available to work with.


skinDetectionAlgorithm = Cheddad2009SkinDetectionAlgorithm()


def get_usage():
    return "Usage:  python3 -m examples.skin_detection_simple_color_threshold file.jpg\n"


if len(sys.argv) == 1:
    print(get_usage())
    exit()

file = sys.argv[1]

image_result, time_spent = skinDetectionAlgorithm.process_resource(Image(file))

# The image_result is an Image object with boundingboxes associated (metadata).
if len(image_result.get_metadata()) == 0:
    print("No skin detected.")

for skin in image_result.get_metadata():
    print("Detected skin, {}".format(skin))
    new_image = Image(file+"_result.jpg", blob_content=skin.get_image().get_blob())
    drawer = SkinDrawer(new_image)
    drawer.amplify()
    new_image.save_to_uri()


print("Process finished in {} seconds".format(time_spent))
