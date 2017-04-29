#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.facedetection.boundingbox.boundingbox import BoundingBox
from src.resource.image.image import Image
import unittest

__author__ = 'Iván de Paz Centeno'


class ImageTest(unittest.TestCase):

    def test_load_save(self):
        image = Image(uri='samples/image1.jpg')
        image.load_from_uri()
        self.assertTrue(image.is_loaded())

        destination = Image(uri='samples/output.jpg', blob_content=image.get_blob())
        destination.save_to_uri()
        self.assertTrue(destination.exists())

    def test_crop_image(self):
        image = Image(uri='samples/image1.jpg')
        image.load_from_uri()

        boundingbox_to_crop = BoundingBox(940, 219, 186, 185)

        cropped = image.crop_image(boundingbox_to_crop, 'samples/result_cropped.jpg')
        cropped.save_to_uri()
        self.assertTrue(cropped.exists())

    def test_load_image_from_route_with_spaces(self):
        spaces_route = "samples/test_routes/spaces/route with spaces/test space.jpg"
        image = Image(uri=spaces_route)
        image.load_from_uri()
        self.assertTrue(image.is_loaded())

    def test_load_image_from_special_route_1(self):
        special_route = "samples/test_routes/specialchars/añ/ñ.jpg"
        image = Image(uri=special_route)
        image.load_from_uri()
        self.assertTrue(image.is_loaded())


if __name__ == '__main__':
    unittest.main()
