#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import optparse

from bin.loader.algorithm.age_estimation_algorithm_loader import AgeEstimationAlgorithmLoader
from bin.loader.dataset.age_estimation_dataset_loader import AgeEstimationDatasetLoader
from src.algorithm.ageestimation.cnn_levi_hassner_age_estimation_algorithm import CNNLeviHassnerAgeEstimationAlgorithm
from src.resource.image.image import Image

__author__ = 'Iván de Paz Centeno'
__version__ = '1.0.0'

# We want to parse the arguments to fill the required data
parser = optparse.OptionParser("Usage: %prog image -a ALGORITHM\n\n"
                               "Example: %prog face_image.jpg -a age_estimation_cnn_levi_hassner", version="%prog {}".format(__version__))
parser.add_option("-x", "--list-available-algorithms", dest="list_algorithms", action="store_true", help="List the currently implemented "
                                                                                    "algorithms to process.")
parser.add_option("-g", "--use-gpu", dest="use_gpu_index", help="Sets the gpu to work for the algorithm (if available and supported). The 0 is the first GPU, the second is the 1 and so on.")
parser.add_option("-a", "--use-algorithm", dest="use_algorithm", help="Specifies the algorithm to use in order to make the estimation. By default the age_estimation_cnn_levi_hassner is used.")

(options, args) = parser.parse_args()

algorithm_loader = AgeEstimationAlgorithmLoader()
dataset_loader = AgeEstimationDatasetLoader()

if options.list_algorithms:
    print("\nAvailable algorithms:\n{}".format(algorithm_loader))
    print("\n")
    parser.print_usage()
    exit()


if len(args) != 1:
    parser.error("An image must be passed.")

file_route = args[0]

if not options.use_algorithm:
    algorithm_id = 'age_estimation_cnn_levi_hassner'
else:
    algorithm_id = options.use_algorithm

print("Using algorithm {}".format(algorithm_id))

algorithm_init_params = {}

if options.use_gpu_index:
    algorithm_init_params['use_gpu'] = int(options.use_gpu_index)
    print("Using GPU ID {}".format(options.use_gpu_index))
    
age_estimation_algorithm = algorithm_loader.get_module(algorithm_id)(**algorithm_init_params)

image_to_process = Image(file_route, "input")

image_result, time_spent = age_estimation_algorithm.process_resource(image_to_process)
time_spent = round(time_spent, 2)

age_result = image_result.get_metadata()[0]

print("Age: {}".format(age_result))
print("Done in {} seconds.".format(time_spent))