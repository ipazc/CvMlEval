#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.genderestimation.gender.gender import GENDER_FEMALE, GENDER_MALE
from src.dataset.simple_adience_dataset import SimpleAdienceDataset

__author__ = 'Iván de Paz Centeno'

import unittest
import os


class SimpleAdienceDatasetTest(unittest.TestCase):

    def setUp(self):
        self.dataset_dir = os.path.join(os.getenv("HOME"), 'adience_simple/')
        self.metadata_file = os.path.join(self.dataset_dir, 'metadata.txt')
        self.dataset = SimpleAdienceDataset(self.dataset_dir, self.metadata_file)
        self.dataset_files_count = len(self.dataset.routes)

    def test_find_image(self):
        routes = self.dataset.find_image_route('2054.10524108124_5d6473f2d1_o.jpg')

        # it must be only one route for this token
        self.assertEqual(len(routes), 1)

        # The returned route must match:
        self.assertEqual(routes[0], os.path.join(self.dataset_dir, 'landmark_aligned_face.2054.10524108124_5d6473f2d1_o.jpg'))

        routes = self.dataset.find_image_route('1000000000')

        # it must be none routes for this token
        self.assertEqual(len(routes), 0)

    def test_formatted_metadata(self):
        formatted_metadata = self.dataset.get_formatted_metadata()

        self.assertEqual(len(formatted_metadata), self.dataset_files_count)

        picture_metadata = formatted_metadata['2054.10524108124_5d6473f2d1_o.jpg']
        self.assertEqual(len(picture_metadata), 2)

        age_range = picture_metadata[0]
        gender = picture_metadata[1]

        self.assertEqual(age_range.get_range(), [25, 32])
        self.assertEqual(gender.get_gender(), GENDER_FEMALE)

        picture_metadata = formatted_metadata['2052.10523995076_ee62d9ae75_o.jpg']
        self.assertEqual(len(picture_metadata), 2)

        age_range = picture_metadata[0]
        gender = picture_metadata[1]

        self.assertEqual(age_range.get_range(), [0, 2])
        self.assertEqual(gender.get_gender(), GENDER_MALE)


if __name__ == '__main__':
    unittest.main()
