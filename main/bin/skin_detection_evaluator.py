#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import optparse
import os

from bin.loader.algorithm.skin_detection_algorithm_loader import SkinDetectionAlgorithmLoader
from bin.loader.dataset.skin_detection_dataset_loader import SkinDetectionDatasetLoader
from src.comparator.skin_comparator import SkinComparator
from src.drawer.skin_drawer import SkinDrawer
from src.report.skin_detection_report import SkinDetectionReport
from src.resource.image.image import Image
from src.version import __version__

__author__ = 'Iván de Paz Centeno'


# Default comparison match_threshold
DEFAULT_MATCH_THRESHOLD = 0.6

# We want to parse the arguments to fill the required data
parser = optparse.OptionParser("Usage: %prog ALGORITHM -d dataset_dir -m metadata_file DATASET\n\n"
                               "Example: %prog skin_detection_simple_color -d dataset/DATASET_NAME -m dataset/DATASET_NAME/metadata[.txt] DATASET_NAME", version="%prog {}".format(__version__))
parser.add_option("-d", "--dataset-root-dir", dest="dataset_dir", help="root directory of the dataset images.")
parser.add_option("-m", "--dataset-metadata-file", dest="metadata_file", help="uri to the metadata file (can be a folder if algorithm needs it).")
parser.add_option("-t", "--match-threshold", dest="match_threshold", help="threshold for comparison matches, "
                                                                          "which ranges from 0.00 to 1.00.")
parser.add_option("-x", "--list-available-algorithms", dest="list_algorithms", action="store_true", help="List the currently implemented "
                                                                                    "algorithms to process.")
parser.add_option("-l", "--list-supported-datasets", dest="list_datasets", action="store_true", help="List the currently supported datasets")
parser.add_option("-s", "--save-images", dest="save_images", action="store_true", help="Saves the processed images with the skin mask applied. The true positive pixels are marked in yellow, the true negatives are marked in blue, the false positives are marked in red and the false negatives in brown.")

(options, args) = parser.parse_args()

algorithm_loader = SkinDetectionAlgorithmLoader()
dataset_loader = SkinDetectionDatasetLoader()

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


detection_algorithm = algorithm_loader.get_module(algorithm_id)()
dataset = dataset_loader.get_module(dataset_id)(dataset_dir, metadata_file)

print("\nDataset: \"{}\""
      "\nDataset Dir: \"{}\""
      "\nMetadata file:\"{}\""
      "\nAlgorithm: \"{}\""
      "\nMatch_threshold:\"{}\"".format(dataset_id, dataset_dir, metadata_file, algorithm_id, match_threshold))

path, filename = os.path.split(dataset_dir)

save_path = path+"_" + detection_algorithm.get_name()
if not os.path.exists(save_path):
    os.mkdir(save_path)

if options.save_images:
    print("Saving images to dir \"{}\"\n".format(save_path))

# Now we take the metadata from the dataset.
metadata = dataset.get_formatted_metadata()

detection_report = SkinDetectionReport("Skin detection", detection_algorithm.get_description(),
                                       dataset.get_description(), match_threshold, "Ignored value. No threshold applied yet")

# And iterate over it.
iteration = 0
for image_id, bounding_boxes in metadata.items():
    iteration += 1
    percent_done = round((iteration/len(metadata)) * 100,2)
    file_route = dataset.find_image_route(image_id)

    # we should never have more than one route for a given image_id.
    if len(file_route) > 1:
        print(file_route)
        parser.error("The image id {} has more than one associated files. Process stopped.".format(image_id))

    if len(file_route) == 0:
        print("No file associated with {} detected.".format(image_id))
        continue

    print("[{}%] Processing \"{}\"...".format(percent_done, file_route[0]), end="")
    image_to_process = Image(file_route[0], image_id, bounding_boxes)
    image_result, time_spent = detection_algorithm.process_resource(image_to_process)
    time_spent = round(time_spent, 2)
    print(" Done in {} seconds. Comparing...".format(time_spent), end="")

    # Let's compare the bounding boxes for each image
    comparator = SkinComparator(match_threshold)
    confusion_matrix, dices_coefficient = comparator.compare_images(image_to_process, image_result)

    skin_ground_truth = image_to_process.get_metadata()[0]
    skin_detected = image_result.get_metadata()[0]

    detection_report.add_result(image_id, skin_ground_truth.get_area(), skin_detected.get_area(),
                                time_spent, dices_coefficient, confusion_matrix.get_true_positives(),
                                confusion_matrix.get_false_positives(),
                                confusion_matrix.get_false_negatives(), confusion_matrix.get_true_negatives(),
                                confusion_matrix.get_accuracy(),
                                confusion_matrix.get_recall(), confusion_matrix.get_precision(),
                                confusion_matrix.get_fallout(), confusion_matrix.get_miss_rate(),
                                confusion_matrix.get_f1_score(), True)

    save_images_text = ""

    # Let's draw the image result for each
    if options.save_images:

        new_uri = image_to_process.get_uri().replace(path, save_path)
        new_uri_path, new_uri_filename = os.path.split(new_uri)

        image_to_save = Image(new_uri, blob_content=skin_detected.get_image().get_blob())
        image_to_save.convert_to_boolean()
        image_to_save.convert_to_uint()
        skin_drawer = SkinDrawer(image_to_save)
        skin_drawer.amplify()

        if not os.path.exists(save_path):
            os.mkdir(new_uri_path)

        image_to_save.save_to_uri()
        save_images_text = " Saved."

    print("[{}].{}".format(confusion_matrix, save_images_text))


face_detection_report_file = os.path.join(save_path, 'report.txt')
detection_report.save_report(face_detection_report_file)
