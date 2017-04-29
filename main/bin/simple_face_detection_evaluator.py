#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import optparse
import os

from bin.loader.algorithm.face_detection_algorithm_loader import FaceDetectionAlgorithmLoader
from bin.loader.dataset.simple_face_detection_dataset_loader import SimpleFaceDetectionDatasetLoader
from src.comparator.face_holder_comparator import FaceHolderComparator
from src.report.simple_face_detection_report import SimpleFaceDetectionReport
from src.resource.image.image import Image
from src.version import __version__

__author__ = 'Iván de Paz Centeno'

"""
In contrast with the main face detection evaluator, this evaluator only evaluates if images hold faces or not.
It doesn't check if the faces detected are in the right position or not.
"""


# Default comparison match_threshold
DEFAULT_MATCH_THRESHOLD = 1

# We want to parse the arguments to fill the required data
parser = optparse.OptionParser("Usage: %prog ALGORITHM -d dataset_dir -m metadata_file DATASET\n\n"
                               "Example: %prog face_detection_dlib -d dataset/AFW_DIR -m dataset/AFW_DIR/metadata.txt AFW", version="%prog {}".format(__version__))
parser.add_option("-d", "--dataset-root-dir", dest="dataset_dir", help="root directory of the AFW Dataset images.")
parser.add_option("-m", "--dataset-metadata-file", dest="metadata_file", help="uri to the metadata file.")
parser.add_option("-t", "--match-threshold", dest="match_threshold", help="threshold for comparison matches, "
                                                                          "which ranges from 0.00 to 1.00")
parser.add_option("-x", "--list-available-algorithms", dest="list_algorithms", action="store_true", help="List the currently implemented "
                                                                                    "algorithms to process.")
parser.add_option("-l", "--list-supported-datasets", dest="list_datasets", action="store_true", help="List the currently supported datasets")
parser.add_option("-s", "--save-images", dest="save_images", action="store_true", help="Saves the processed images with the bounding boxes drawn. The URI is the same as the dataset dir specified with the -d parameter, but with the name of the algorithm appended. For example, for opencv in an 'AFW/' dataset, the result will be stored in 'AFW_opencv/'. The blue box indicates the labeled face in the dataset, the red box is the detected face and the green box is the intersection between both. The percentage shown is the rate of intersection with the smallest box.")

(options, args) = parser.parse_args()

algorithm_loader = FaceDetectionAlgorithmLoader()
dataset_loader = SimpleFaceDetectionDatasetLoader()

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
    parser.error("Algorithm and dataset must be specified. \nCheck the available algorithms with the -x flag and the supported datasets with -l")


algorithm_id = args[0]
dataset_id = args[1]

if not algorithm_loader.does_module_exist(algorithm_id):
    parser.error("Algorithm {} not implemented.".format(algorithm_id))

if not dataset_loader.does_module_exist(dataset_id):
    parser.error("Dataset parser for {} not available.".format(dataset_id))


face_detection_algorithm = algorithm_loader.get_module(algorithm_id)()
dataset = dataset_loader.get_module(dataset_id)(dataset_dir, metadata_file)

print("\nDataset: \"{}\""
      "\nDataset Dir: \"{}\""
      "\nMetadata file:\"{}\""
      "\nAlgorithm: \"{}\""
      "\nMatch_threshold:\"{}\"".format(dataset_id, dataset_dir, metadata_file, algorithm_id, match_threshold))

path, filename = os.path.split(dataset_dir)

save_path = path+"_"+face_detection_algorithm.get_name()

# Now we take the metadata from the dataset.
metadata = dataset.get_formatted_metadata()

face_detection_report = SimpleFaceDetectionReport("Simple face detection", face_detection_algorithm.get_description(),
                                                  dataset.get_description())

# And iterate over it.
iteration = 0
for image_id, has_faces_metadata in metadata.items():
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
    image_to_process = Image(file_route[0], image_id, has_faces_metadata)
    image_result, time_spent = face_detection_algorithm.process_resource(image_to_process)
    time_spent = round(time_spent, 2)
    print(" Done in {} seconds. Comparing...".format(time_spent), end="")

    # Let's compare the bounding boxes for each image
    face_holder_comparator = FaceHolderComparator()
    true_positives, false_positives, false_negatives, true_negatives = face_holder_comparator.compare_images(
        image_to_process, image_result)

    face_detection_report.add_result(image_id, has_faces_metadata[0], len(image_result.get_metadata()) > 0,
                                     time_spent, true_positives, false_positives,
                                     false_negatives, true_negatives)

    print(" [{} true positives, {} false positives {} false negatives {} true negatives].".format(true_positives, false_positives,
                                                                                  false_negatives, true_negatives))

if not os.path.exists(save_path):
    os.mkdir(save_path)

face_detection_report_file = os.path.join(save_path, 'report.txt')
face_detection_report.save_report(face_detection_report_file)
