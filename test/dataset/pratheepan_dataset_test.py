#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os
from src.dataset.pratheepan_dataset import PratheepanDataset

__author__ = 'Iván de Paz Centeno'


class PratheepanDatasetTest(unittest.TestCase):

    def setUp(self):
        self.dataset_dir = os.path.join(os.getenv("HOME"), 'skin_datasets/Pratheepan_Dataset/')
        self.metadata_dir = os.path.join(os.getenv("HOME"), 'skin_datasets/Ground_Truth/')

        self.dataset = PratheepanDataset(self.dataset_dir, self.metadata_dir)
        self.dataset_files_count = len(self.dataset.routes)

    def test_find_image(self):
        routes = self.dataset.find_image_route('w_sexy.jpg')

        # it must be only one route for this token
        self.assertEqual(len(routes), 1)

        # The returned route must exist:
        self.assertTrue(os.path.exists(routes[0]))

        routes = self.dataset.find_image_route('vick-family.jpg')

        # it must be only one route for this token
        self.assertEqual(len(routes), 1)

        # The returned route must exist:
        self.assertTrue(os.path.exists(routes[0]))

        routes = self.dataset.find_image_route('1000000000')

        # it must be none routes for this token
        self.assertEqual(len(routes), 0)

    def test_formatted_metadata(self):
        formatted_metadata = self.dataset.get_formatted_metadata()

        self.assertEqual(len(formatted_metadata), self.dataset_files_count)

        picture_metadata = formatted_metadata['vick-family.jpg']
        self.assertEqual(len(picture_metadata), 1)

        picture_skin = picture_metadata[0]

        self.assertEqual(picture_skin.get_area(), 5962410)

        picture_metadata = formatted_metadata['w_sexy.jpg']
        self.assertEqual(len(picture_metadata), 1)

        picture_skin = picture_metadata[0]
        self.assertEqual(picture_skin.get_area(), 4826130)

if __name__ == '__main__':
    unittest.main()
