#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fnmatch
import os

from src.algorithm.skindetection.skin.skin import Skin
from src.dataset.dataset import Dataset
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'


class PratheepanDataset(Dataset):

    def __init__(self, root_folder, metadata_folder):
        """
        Loads the dataset metadata into memory.

        :param root_folder: folder at which the images are going to be located.
        :param metadata_folder:  folder at which the ground-truth is set.
        """
        Dataset.__init__(self, root_folder, metadata_folder, 'Pratheepan dataset for skin detection.')

        self.skin_mask_default_extension = '.png'

        # methods to load the routes recursively, and metadata

        self.__load_routes__()  # routes are saved in self.routes
        self.__load_metadata_file__()  # metadata content is saved in self.metadata_content

    def __load_metadata_file__(self):

        # The metadata content for this dataset is just a folder with skin masks.
        # The names of the mask files is the image_id

        # The convention is to have a metadata file, but for this dataset it is a folder.
        metadata_folder = self.metadata_file

        for root, dirnames, filenames in os.walk(metadata_folder):

            for filename in fnmatch.filter(filenames, "*" + self.skin_mask_default_extension):

                image_id = os.path.splitext(filename)[0] + self.default_extension
                self.metadata_content.append([image_id, os.path.join(root, filename)])

    def find_image_route(self, image_id):
        """
        finds the specified image id token inside the routes.

        :param image_id: id token to search for.
        :return: routes that matches the specified id token. It may return more than one image route if
        the ID is not specific enough.
        """
        search_key = "/" + image_id
        return [route for route in self.routes if search_key in route]

    def get_formatted_metadata(self):
        """
        Formats the current metadata content into a processable metadata in a dictionary form (key->value)

        :return: a dictionary of formatted metadata entries.
        """

        formatted_metadata = {}

        for [image_id, metadata_line] in self.metadata_content:
            skin_mask_image = Image(metadata_line, image_id=image_id)

            # We don't load the skin mask to memory, since we want to save resources.
            # That's the reason
            # Let's make a lazy load and delegate it to the moment at which it's going to be processed.
            skin_mask = Skin(skin_mask_image)

            metadata_element = [skin_mask]

            if image_id in formatted_metadata:
                # A skin mask already registered for this image.
                # Let's add a second skin mask
                formatted_metadata[image_id] = formatted_metadata[image_id] + metadata_element
            else:
                formatted_metadata[image_id] = metadata_element

        return formatted_metadata
