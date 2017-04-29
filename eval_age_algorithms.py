#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import numpy as np

from main.model.algorithm.estimation.age.api_rest_age_estimation import APIRESTAgeEstimationAlgorithm
from main.model.comparator.age_range_comparator import AgeRangeComparator
from main.model.dataset.lowaged_dataset import LowAgedDataset
from main.model.resource.image import Image
from main.model.tools.age_range import AgeRange
from main.services.image.algorithm_service import ImageAlgorithmService

__author__ = "Ivan de Paz Centeno"

low_aged_dataset = LowAgedDataset('/home/ivan/Desktop/adience/good_low_aged',
                                  '/home/ivan/Desktop/adience/good_low_aged/metadata_lowaged.json')

real_rothe_service = ImageAlgorithmService(APIRESTAgeEstimationAlgorithm, pool_limit=4,
                                               api_url='http://192.168.2.110:9095/estimation-requests/age/face/stream?service=gpu-cnn-rothe-real-age-estimation',
                                               name="rothe_real_age", description="Rothe real")

apparent_rothe_service = ImageAlgorithmService(APIRESTAgeEstimationAlgorithm, pool_limit=4,
                                               api_url='http://192.168.2.110:9095/estimation-requests/age/face/stream?service=gpu-cnn-rothe-apparent-age-estimation',
                                               name="rothe_apparent_age", description="Rothe apparent")

ivan_service = ImageAlgorithmService(APIRESTAgeEstimationAlgorithm, pool_limit=4,
                                               api_url='http://192.168.2.110:9095/estimation-requests/age/face/stream?service=gpu-cnn-depaz-age-estimation',
                                               name="ivan_lowage", description="Ivan lowage model")

real_rothe_service.start()
apparent_rothe_service.start()
ivan_service.start()

service = apparent_rothe_service; algorithm_name="Rothe's apparent"

images = low_aged_dataset.get_images()
print("Images loaded from dataset: {}".format(len(images)))

comparator = AgeRangeComparator(0.5)
hit_count = 0


def split_by_age_ranges(list_images):
    images_dict = {}

    for image in list_images:
        age_range_vector = image.get_metadata()[0].get_range()
        age_range_str = str(age_range_vector)

        if age_range_str not in images_dict:
            images_dict[age_range_str] = []

        images_dict[age_range_str].append(image)

    return images_dict

images_dict = split_by_age_ranges(images)

for age_range_vect, images_list in images_dict.items():
    age_range = AgeRange.from_string(age_range_vect)
    promises = []
    images_queued = 0
    count = len(images_list)
    hit_count = 0
    age_means = []

    for image_tmp in images_list:
        image = image_tmp.clone()
        image.load_from_uri()

        promises.append(service.append_request(image))
        images_queued += 1

        print("\rProcessing {}/{} images in age range {}..".format(images_queued, count, age_range_vect), end="", flush=True)

    iteration = 0
    for promise, image in zip(promises, images_list):
        iteration += 1
        result, time_spent = promise.get_resource()
        age_means.append(result.get_metadata()[0].get_mean())

        _, tp, fp, fn = comparator.compare_images(image, result)
        hit_count += tp
        print("\r[{}%] {} took {} seconds for {}. Result is: {} (hit: {})".format(round(iteration/count*100,2),algorithm_name, round(time_spent, 2), "{}/{}".format(
            image.get_uri().split("/")[-2], image.get_uri().split("/")[-1]), result.get_metadata()[0], tp > 0), end="", flush=True)

    absolute_errors = [abs(mean - image.get_metadata()[0].get_mean()) for mean, image in zip(age_means, images_list)]
    full_mean = np.mean(age_means)
    variance = np.mean([(val-full_mean) * (val-full_mean) for val in age_means])
    typical_deviation = np.sqrt(variance)
    mae = np.mean(absolute_errors)

    print("\n----------------------------------")
    print("Range {}".format(age_range_vect))
    print("\nTotal hits for {}: {}".format(age_range_vect, hit_count))
    print("Total failures for {}: {}".format(age_range_vect, count - hit_count))
    print("Mean: {}".format(round(full_mean, 4)).replace(".",","))
    print("Variance: {}".format(round(variance, 4)).replace(".",","))
    print("Typical deviation: {}".format(round(typical_deviation, 4)).replace(".",","))
    print("MAE: {}".format(round(mae, 4)).replace(".",","))
    print("Accuracy: {}%".format(round(hit_count / count * 100, 4)).replace(".",","))
    print("----------------------------------\n")

"""
#images = split_half(images)[1]
promises = []

images_queued = 0
for image_tmp in images:
    image = image_tmp.clone()
    image.load_from_uri()

    promises.append(service.append_request(image))
    images_queued += 1

    print("\rProcessing {} images..".format(images_queued), end="", flush=True)

print("\nreached this point")

for promise, image in zip(promises, images):
    result, time_spent = promise.get_resource()

    _, tp, fp, fn = comparator.compare_images(image, result)
    hit_count += tp
    print ("Real's took {} seconds for {}. Result is: {} (hit: {})".format(round(time_spent,2), "{}/{}".format(image.get_uri().split("/")[-2], image.get_uri().split("/")[-1]), result.get_metadata()[0], tp > 0))

"""

real_rothe_service.stop()
apparent_rothe_service.stop()
ivan_service.stop()
"""
result, time_spent = apparent_rothe.process_resource(image)
print ("Rothe apparent took {} seconds. Result is: {}".format(time_spent, result.get_metadata()[0]))

result, time_spent = ivan_lowage.process_resource(image)
print ("Ivan lowage took {} seconds. Result is: {}".format(time_spent, result.get_metadata()[0]))
"""