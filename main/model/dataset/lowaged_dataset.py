#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

from main.model.dataset.dataset import Dataset
from main.model.resource.image import Image
from main.model.tools.age_range import AgeRange

__author__ = 'Iván de Paz Centeno'


class LowAgedDataset(Dataset):
    def __init__(self, root_folder, metadata_file):
        """
        Loads the dataset metadata into memory.

        :param root_folder: folder at which the images are going to be located.
        :param metadata_file:  filename of the metadata file
        """
        Dataset.__init__(self, root_folder, metadata_file, 'Reduced Adience Dataset for low age tests (0-12 yo).')

        # methods to load the routes recursively, and metadata

        self.__load_routes__()  # routes are saved in self.routes
        self.__load_metadata_file__()  # metadata content is saved in self.metadata_content

    def find_image_route(self, image_id):
        """
        finds the specified image id token inside the routes.

        :param image_id: id token to search for.
        :return: routes that matches the specified id token. It may return more than one image route if
        the ID is not specific enough.
        """
        search_key = image_id  # + self.default_extension
        return [route for route in self.routes if search_key in route]

    def get_images(self):
        """
        :return: images list with all the age ranges.
        """

        return [Image(uri=os.path.join(self.root_folder,
                                       "{}-{}".format(*AgeRange.from_string(age).get_range()),
                                       path.split("/")[1]),
                      metadata=[AgeRange.from_string(age)])
                for age, paths in json.loads(self.metadata_content).items() for path in paths]