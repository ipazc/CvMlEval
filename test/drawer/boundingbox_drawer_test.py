#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.facedetection.boundingbox.boundingbox import BoundingBox
from src.drawer.boundingbox_drawer import BoundingboxDrawer
from src.drawer.drawer import COLOR_BLUE, COLOR_RED, COLOR_GREEN
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'

import unittest


class BoundingboxDrawerTest(unittest.TestCase):

    def setUp(self):
        # We need to load an image to draw the bounding boxes.
        self.image = Image(uri='samples/image1.jpg')
        self.image.load_from_uri()
        self.boundingbox_drawer = BoundingboxDrawer(self.image)

    def test_draw_boundingbox(self):
        boundingbox_expected = [BoundingBox(940, 219, 186, 185),
                                BoundingBox(1533, 493, 268, 268),
                                BoundingBox(485, 485, 223, 223)]
        boundingbox_calculated = [BoundingBox(467, 505, 223, 223),
                                  BoundingBox(945, 223, 181, 197),
                                  BoundingBox(1589, 517, 233, 225)]
        boundingbox_intersection = [BoundingBox(945, 223, 181, 181),
                                    BoundingBox(1589, 517, 212, 225),
                                    BoundingBox(485, 505, 205, 203)]

        intersections_percentage = [0.9521, 0.9099, 0.8368]

        for boundingbox1, boundingbox2, boundingbox3, percentage in zip(boundingbox_expected, boundingbox_calculated,
                                                                        boundingbox_intersection,
                                                                        intersections_percentage):

            self.boundingbox_drawer.draw_boundingbox(boundingbox1, COLOR_BLUE)
            self.boundingbox_drawer.draw_boundingbox(boundingbox2, COLOR_RED)
            self.boundingbox_drawer.draw_boundingbox(boundingbox3, COLOR_GREEN)
            self.boundingbox_drawer.draw_text(boundingbox3.get_center(), "{}%".format(round(percentage*100,2)))

        image_to_save = Image(uri='samples/drawn.jpg', blob_content=self.image.get_blob())
        image_to_save.save_to_uri()
        self.assertTrue(image_to_save.exists())

if __name__ == '__main__':
    unittest.main()
