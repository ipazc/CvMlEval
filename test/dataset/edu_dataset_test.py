#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os
from src.dataset.edu_dataset import EduDataset

__author__ = 'Iván de Paz Centeno'


class EduDatasetTest(unittest.TestCase):

    def setUp(self):
        self.dataset_dir = os.path.join(os.getenv("HOME"), 'Simple_Face/')
        self.metadata_file = os.path.join(self.dataset_dir, 'gt.csv')
        self.dataset = EduDataset(self.dataset_dir, self.metadata_file)
        self.dataset_files_count = len(self.dataset.routes)

    def test_find_image(self):
        routes = self.dataset.find_image_route('000244.jpg')

        # it must be only one route for this token
        self.assertEqual(len(routes), 1)

        # The returned route must match:
        self.assertEqual(routes[0], os.path.join(self.dataset_dir, '000244.jpg'))

        routes = self.dataset.find_image_route('1000000000')

        # it must be none routes for this token
        self.assertEqual(len(routes), 0)

    def test_formatted_metadata(self):
        formatted_metadata = self.dataset.get_formatted_metadata()

        self.assertEqual(len(formatted_metadata), self.dataset_files_count)

        picture_metadata = formatted_metadata['000244.jpg']
        self.assertEqual(len(picture_metadata), 1)

        self.assertEqual(picture_metadata[0], False)

        picture_metadata = formatted_metadata['56054945.jpg']
        self.assertEqual(len(picture_metadata), 1)
        self.assertEqual(picture_metadata[0], True)


if __name__ == '__main__':
    unittest.main()
