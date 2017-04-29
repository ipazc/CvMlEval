#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.algorithm.ageestimation.agerange.age_range import AgeRange
from src.algorithm.genderestimation.gender.gender import Gender

__author__ = 'Iván de Paz Centeno'

from src.dataset.dataset import Dataset


class SimpleAdienceDataset(Dataset):
    def __init__(self, root_folder, metadata_file):
        """
        Loads the dataset metadata into memory.

        :param root_folder: folder at which the images are going to be located.
        :param metadata_file:  filename of the metadata file
        """
        Dataset.__init__(self, root_folder, metadata_file, 'Reduced Adience Dataset for simple tests.')

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

    def get_formatted_metadata(self):
        """
        Formats the current metadata content into a processable metadata in a dictionary form (key->value)

        :return: a dictionary of formatted metadata entries.
        """

        formatted_metadata = {}

        for metadata_line in self.metadata_content:

            # to parse metadata_line, we know that tabs are the separators
            values = metadata_line.split('\t')

            file_id = "{}.{}".format(values[2], values[1])

            age_range = AgeRange.from_string(values[3])
            gender = Gender.from_string(values[4])

            metadata_element = [age_range, gender]

            if file_id in formatted_metadata:
                # An age range and gender already loaded for this image.
                # Let's add a second pair.
                formatted_metadata[file_id] = formatted_metadata[file_id] + metadata_element
            else:
                formatted_metadata[file_id] = metadata_element

        return formatted_metadata
