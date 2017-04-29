#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import optparse
import os

from bin.loader.algorithm.gender_estimation_algorithm_loader import GenderEstimationAlgorithmLoader
from bin.loader.dataset.gender_estimation_dataset_loader import GenderEstimationDatasetLoader
from src.comparator.gender_comparator import GenderComparator
from src.report.gender_estimation_report import GenderEstimationReport
from src.resource.image.image import Image
from src.version import __version__

__author__ = 'Iván de Paz Centeno'


# Default comparison match_threshold
DEFAULT_MATCH_THRESHOLD = 1

# We want to parse the arguments to fill the required data
parser = optparse.OptionParser("Usage: %prog ALGORITHM -d dataset_dir -m metadata_file DATASET\n\n"
                               "Example: %prog gender_estimation_cnn_levi_hassner -d dataset/AFW_DIR -m dataset/AFW_DIR/metadata.txt AFW", version="%prog {}".format(__version__))
parser.add_option("-d", "--dataset-root-dir", dest="dataset_dir", help="root directory of the AFW Dataset images.")
parser.add_option("-m", "--dataset-metadata-file", dest="metadata_file", help="uri to the metadata file.")
parser.add_option("-t", "--match-threshold", dest="match_threshold", help="threshold for comparison matches, "
                                                                          "which ranges from 0.00 to 1.00")
parser.add_option("-x", "--list-available-algorithms", dest="list_algorithms", action="store_true", help="List the currently implemented "
                                                                                    "algorithms to process.")
parser.add_option("-l", "--list-supported-datasets", dest="list_datasets", action="store_true", help="List the currently supported datasets")
parser.add_option("-g", "--use-gpu", dest="use_gpu_index", help="Sets the gpu to work for the algorithm (if available and supported). The 0 is the first GPU, the second is the 1 and so on.")

(options, args) = parser.parse_args()

algorithm_loader = GenderEstimationAlgorithmLoader()
dataset_loader = GenderEstimationDatasetLoader()

if options.list_algorithms:
    print("\nAvailable algorithms:\n{}".format(algorithm_loader))

if options.list_datasets:
    print("\nSupported datasets:\n{}".format(dataset_loader))

if options.list_datasets or options.list_algorithms:
    print("\n")
    parser.print_usage()
    exit()

if not options.dataset_dir:
    parser.error("Dataset dir required.")
else:
    dataset_dir = options.dataset_dir
    if not dataset_dir.endswith("/"):
        dataset_dir += "/"

if not options.metadata_file:
    parser.error("Dataset metadata file required.")
else:
    metadata_file = options.metadata_file

if not options.match_threshold:
    match_threshold = DEFAULT_MATCH_THRESHOLD
    print("No comparison matching threshold specified, falling back to the default of {}".format(match_threshold))
else:
    match_threshold = options.match_threshold

if len(args) != 2:
    parser.error("Algorithm and dataset must be specified. \nCheck the available algorithms with the -x flag and the "
                 "supported datasets with -l")


algorithm_id = args[0]
dataset_id = args[1]

if not algorithm_loader.does_module_exist(algorithm_id):
    parser.error("Algorithm {} not implemented.".format(algorithm_id))

if not dataset_loader.does_module_exist(dataset_id):
    parser.error("Dataset parser for {} not available.".format(dataset_id))

algorithm_init_params = {}

if options.use_gpu_index:
    algorithm_init_params['use_gpu'] = options.use_gpu_index

gender_estimation_algorithm = algorithm_loader.get_module(algorithm_id)(**algorithm_init_params)

dataset = dataset_loader.get_module(dataset_id)(dataset_dir, metadata_file)

print("\nDataset: \"{}\""
      "\nDataset Dir: \"{}\""
      "\nMetadata file:\"{}\""
      "\nAlgorithm: \"{}\""
      "\nMatch_threshold:\"{}\"".format(dataset_id, dataset_dir, metadata_file, algorithm_id, match_threshold))

path, filename = os.path.split(dataset_dir)

save_path = path+"_"+gender_estimation_algorithm.get_name()

# Now we take the metadata from the dataset.
metadata = dataset.get_formatted_metadata()

gender_estimation_report = GenderEstimationReport("Gender estimation", gender_estimation_algorithm.get_description(),
                                                  dataset.get_description())

# And iterate over it.
iteration = 0
for image_id, [age_range, gender] in metadata.items():
    iteration += 1
    percent_done = round((iteration/len(metadata)) * 100, 2)
    file_route = dataset.find_image_route(image_id)

    # we should never have more than one route for a given image_id.
    if len(file_route) > 1:
        print(file_route)
        parser.error("The image id {} has more than one associated files. Process stopped.".format(image_id))

    if len(file_route) == 0:
        print("No file associated with {} detected.".format(image_id))
        continue

    print("[{}%] Processing \"{}\"...".format(percent_done, file_route[0]), end="")
    image_to_process = Image(file_route[0], image_id, [gender])
    image_result, time_spent = gender_estimation_algorithm.process_resource(image_to_process)
    time_spent = round(time_spent, 2)
    print(" Done in {} seconds. Comparing...".format(time_spent), end="")

    # Let's compare the genders
    gender_range_comparator = GenderComparator()
    intersections, true_positives, false_positives, false_negatives = gender_range_comparator.compare_images(
        image_to_process, image_result)

    gender_estimation_report.add_result(image_id, gender, image_result.get_metadata()[0],
                                        time_spent, true_positives, false_positives,
                                        false_negatives)

    print(" [{} true positives, {} false positives {} false negatives]".format(true_positives, false_positives,
                                                                               false_negatives))

if not os.path.exists(save_path):
    os.mkdir(save_path)
    
gender_estimation_report_file = os.path.join(save_path, 'report.txt')
gender_estimation_report.save_report(gender_estimation_report_file)
