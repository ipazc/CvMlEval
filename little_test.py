#!/usr/bin/env python
# -*- coding: utf-8 -*-
import timeit

from main.model.algorithm.estimation.age.api_rest_age_estimation import APIRESTAgeEstimationAlgorithm
from main.model.comparator.age_range_comparator import AgeRangeComparator
from main.model.resource.image import Image
from main.model.tools.age_range import AgeRange
from timeit import default_timer as timer
from main.services.image.algorithm_service import ImageAlgorithmService

__author__ = "Ivan de Paz Centeno"


age_estimation_service = ImageAlgorithmService(APIRESTAgeEstimationAlgorithm, pool_limit=4,
                                               api_url='http://192.168.2.110:9095/estimation-requests/age/face/stream?service=gpu-cnn-rothe-real-age-estimation',
                                               name="rothe_real_age", description="Rothe real")
age_estimation_service.start()

images = [Image(uri="/home/ivan/trash/4.jpe"),
          Image(uri="/home/ivan/trash/6.jpe"),
          Image(uri="/home/ivan/trash/2.jpe"),
          Image(uri="/home/ivan/trash/edu2rne.jpg")]
for image in images: image.load_from_uri()

resource_promises = [age_estimation_service.append_request(image) for image in images]

initial_time = timer()
for resource_promise in resource_promises:
    result, time_spent = resource_promise.get_resource()

    print("Time spent: {} seconds".format(round(time_spent,2)))

    if result.get_uri()=="error":
        print(result.get_id())
    else:
        print(result.get_metadata()[0])
end_time = timer() - initial_time

print(end_time)
age_estimation_service.stop(True)

#resource_promises[1].get_resource()

"""
image1 = Image(metadata=[AgeRange(13,14)])
image2 = Image(metadata=[AgeRange(7,13)])

result = AgeRange(6,6).intersect_with(AgeRange(7,13))
print(result)
print(result.get_distance())
age_range_comparator = AgeRangeComparator(0.5)
print(age_range_comparator.compare_images(image1, image2))
"""