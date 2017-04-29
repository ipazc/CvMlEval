#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os

from src.dataset.afw_dataset import AFWDataset


__author__ = 'Iván de Paz Centeno'


class AFWDatasetTest(unittest.TestCase):

    def setUp(self):
        self.dataset_dir = os.path.join(os.getenv("HOME"), 'AFW/')
        self.metadata_file = os.path.join(self.dataset_dir, 'gt_AFW.txt')
        self.dataset = AFWDataset(self.dataset_dir, self.metadata_file)
        self.dataset_files_count = len(self.dataset.routes)

    def test_find_image(self):
        routes = self.dataset.find_image_route('4337161543')

        # it must be only one route for this token
        self.assertEqual(len(routes), 1)

        # The returned route must match:
        self.assertEqual(routes[0], os.path.join(self.dataset_dir, '4337161543' + self.dataset.default_extension))

        routes = self.dataset.find_image_route('1000000000')

        # it must be none routes for this token
        self.assertEqual(len(routes), 0)

    def test_formatted_metadata(self):
        formatted_metadata = self.dataset.get_formatted_metadata()

        self.assertEqual(len(formatted_metadata), self.dataset_files_count)

        picture_metadata = formatted_metadata['4906266640']
        self.assertEqual(len(picture_metadata), 2)

        self.assertEqual(picture_metadata[0].get_box(), [937, 775, 193, 169])
        self.assertEqual(picture_metadata[1].get_box(), [1865, 687, 197, 213])

        picture_metadata = formatted_metadata['5106695994']
        self.assertEqual(len(picture_metadata), 6)

        picture_metadata = formatted_metadata['255360810']
        self.assertEqual(len(picture_metadata), 1)


if __name__ == '__main__':
    unittest.main()
