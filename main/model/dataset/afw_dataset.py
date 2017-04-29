#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Iván de Paz Centeno'

from src.dataset.dataset import Dataset
from src.algorithm.facedetection.boundingbox.boundingbox import BoundingBox


class AFWDataset(Dataset):
    def __init__(self, root_folder, metadata_file):
        """
        Loads the dataset metadata into memory.

        :param root_folder: folder at which the images are going to be located.
        :param metadata_file:  filename of the metadata file
        """
        Dataset.__init__(self, root_folder, metadata_file, 'Annotated Faces in the Wild')

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
        search_key = image_id + self.default_extension
        return [route for route in self.routes if search_key in route]

    def get_formatted_metadata(self):
        """
        Formats the current metadata content into a processable metadata in a dictionary form (key->value)

        :return: a dictionary of formatted metadata entries.
        """

        formatted_metadata = {}

        for metadata_line in self.metadata_content:

            # to parse metadata_line, we know that spaces are the separators
            values = metadata_line.split()

            file_id = values[0]

            x = int(float(values[1]))
            y = int(float(values[2]))
            width = int(float(values[3]))
            height = int(float(values[4]))

            metadata_element = [BoundingBox(x, y, width, height)]

            if file_id in formatted_metadata:
                # A bounding box already registered for this image.
                # Let's add a second bounding box
                formatted_metadata[file_id] = formatted_metadata[file_id] + metadata_element
            else:
                formatted_metadata[file_id] = metadata_element

        return formatted_metadata
