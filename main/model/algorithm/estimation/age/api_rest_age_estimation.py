#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from main.model.algorithm.algorithm import Algorithm
from main.model.algorithm.image_algorithm import ImageAlgorithm
from main.model.tools.age_range import AgeRange

__author__ = "Ivan de Paz Centeno"

class APIRESTAgeEstimationAlgorithm(ImageAlgorithm):
    """
    Wraps an age estimation call to an APIRest
    """

    def __init__(self, api_url, name, description):

        Algorithm.__init__(self, name, description)
        self.api_url = api_url

    def _process_resource(self, image):
        """
        Processes the specified image in order to get the estimation from the API-REST.
        :param image: image resource pointing to a valid URI or containing the image content.
                    If the image is not loaded but is pointing to a valid URI, this method
                    will try to load the image from the URI in grayscale.
        :return: the estimation result wrapped in a list
        """
        response = requests.put(self.api_url, data=image.get_jpeg(), verify=False)

        if response.status_code != 200:
            raise Exception("[Backend ({}) for {}] {}!".format(self.api_url, self.get_name(),
                                                                                           response.json()['message']))
        response_json = json.loads(response.text)

        if 'Age_range' not in response_json:
            raise Exception("This caller does not understand backend's language. It may be a different version.")

        age_range = AgeRange.from_string(response_json['Age_range'])

        return [age_range]
