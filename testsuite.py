#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import unittest

from test.agerange.age_range_test import AgeRangeTest
from test.algorithm.ageestimation.cnn_levi_hassner_age_estimation_algorithm_test import \
    CNNLeviHassnerAgeEstimationAlgorithmTest
from test.algorithm.ageestimation.cnn_rothe_apparent_age_estimation_algorithm_test import \
    CNNRotheApparentAgeEstimationAlgorithmTest
from test.algorithm.ageestimation.cnn_rothe_real_age_estimation_algorithm_test import \
    CNNRotheRealAgeEstimationAlgorithmTest
from test.algorithm.facedetection.dlib_face_detection_algorithm_test import DLibFaceDetectionAlgorithmTest
from test.algorithm.facedetection.neven_face_detection_algorithm_test import NevenFaceDetectionAlgorithmTest
from test.algorithm.facedetection.opencv_face_detection_algorithm_test import OpenCVFaceDetectionAlgorithmTest
from test.algorithm.genderestimation.cnn_levi_hassner_gender_estimation_algorithm_test import \
    CNNLeviHassnerGenderEstimationAlgorithmTest
from test.algorithm.genderestimation.cnn_rothe_gender_estimation_algorithm_test import \
    CNNRotheGenderEstimationAlgorithmTest
from test.algorithm.imageclassification.bow_svm_image_classificaton_linear_kernel_algorithm_test import \
    BowSVMImageClassificationLinearKernelAlgorithmTest
from test.algorithm.imageclassification.bow_svm_image_classificaton_poly5_kernel_algorithm_test import \
    BowSVMImageClassificationPoly5KernelAlgorithmTest
from test.algorithm.imageclassification.bow_svm_image_classificaton_rbf_kernel_algorithm_test import \
    BowSVMImageClassificationRBFKernelAlgorithmTest
from test.algorithm.skindetection.bayes_lut_dempster_shafer_skin_detection_algorithm_test import \
    BayesLutDempsterShaferSkinDetectionAlgorithmTest
from test.algorithm.skindetection.bayes_lut_skin_detection_algorithm_test import BayesLutSkinDetectionAlgorithmTest
from test.algorithm.skindetection.chai_1999_skin_detection_algorithm_test import Chai1999SkinDetectionAlgorithmTest
from test.algorithm.skindetection.cheddad_2009_skin_detection_algorithm_test import \
    Cheddad2009SkinDetectionAlgorithmTest
from test.algorithm.skindetection.gaussian_distributed_skin_detection_algorithm_test import \
    GaussianDistributedSkinDetectionAlgorithmTest
from test.algorithm.skindetection.hsieh_2002_skin_detection_algorithm_test import Hsieh2002SkinDetectionAlgorithmTest
from test.algorithm.skindetection.kovak_2003_fl_skin_detection_algorithm_test import \
    Kovak2003FLSkinDetectionAlgorithmTest
from test.algorithm.skindetection.kovak_2003_ud_skin_detection_algorithm_test import \
    Kovak2003UDSkinDetectionAlgorithmTest
from test.algorithm.skindetection.simple_color_threshold_skin_detection_algorithm_test import \
    SimpleColorThresholdSkinDetectionAlgorithmTest
from test.algorithm.skindetection.soriano_2000_skin_detection_algorithm_test import \
    Soriano2000SkinDetectionAlgorithmTest
from test.algorithm.textclassification.bow_logistic_regression_text_classification_algorithm_test import \
    BowLogisticRegressionTextClassificationAlgorithmTest
from test.algorithm.textclassification.bow_naive_bayes_text_classification_algorithm_test import \
    BowNaiveBayesTextClassificationAlgorithmTest
from test.algorithm.textclassification.bow_support_vector_machine_text_classification_algorithm_test import \
    BowSVMTextClassificationAlgorithmTest
from test.algorithm.textclassification.hashing_logistic_regression_text_classification_algorithm_test import \
    HashingLogisticRegressionTextClassificationAlgorithmTest
from test.algorithm.textclassification.hashing_support_vector_machine_text_classification_algorithm_test import \
    HashingSVMTextClassificationAlgorithmTest
from test.algorithm.textclassification.tfidf_logistic_regression_text_classification_algorithm_test import \
    TFIDFLogisticRegressionTextClassificationAlgorithmTest
from test.algorithm.textclassification.tfidf_naive_bayes_text_classification_algorithm_test import \
    TFIDFNaiveBayesTextClassificationAlgorithmTest
from test.algorithm.textclassification.tfidf_support_vector_machine_text_classification_algorithm_test import \
    TFIDFSVMTextClassificationAlgorithmTest
from test.boundingbox.boundingbox_test import BoundingBoxTest
from test.comparator.age_range_comparator_test import AgeRangeComparatorTest
from test.comparator.face_boundingbox_comparator_test import FaceBoundingBoxComparatorTest
from test.comparator.gender_comparator_test import GenderComparatorTest
from test.dataset.afw_dataset_test import AFWDatasetTest
from test.dataset.edu_dataset_test import EduDatasetTest
from test.dataset.pratheepan_dataset_test import PratheepanDatasetTest
from test.dataset.simple_adience_dataset_test import SimpleAdienceDatasetTest
from test.drawer.boundingbox_drawer_test import BoundingboxDrawerTest
from test.face_detection_report_test import FaceDetectionReportTest
from test.resource.image.image_test import ImageTest
from test.skin.skin_test import SkinTest

__author__ = 'Iván de Paz Centeno'


config_file = 'modules.cfg'

available_modules = {'boundingbox': BoundingBoxTest,
                     'agerange': AgeRangeTest,
                     'skin': SkinTest,

                     # DATASETS
                     'afwdataset': AFWDatasetTest,
                     'simple_adience_dataset': SimpleAdienceDatasetTest,
                     'edu_dataset': EduDatasetTest,
                     'pratheepan_dataset': PratheepanDatasetTest,

                     # FACE DETECTION ALGORITHMS
                     'dlibfacedetection': DLibFaceDetectionAlgorithmTest,
                     'opencvfacedetection': OpenCVFaceDetectionAlgorithmTest,
                     'nevenfacedetection': NevenFaceDetectionAlgorithmTest,

                     # AGE ESTIMATION ALGORITHMS
                     'levi_hassner_age_estimation': CNNLeviHassnerAgeEstimationAlgorithmTest,
                     'rothe_real_age_estimation': CNNRotheRealAgeEstimationAlgorithmTest,
                     'rothe_apparent_age_estimation': CNNRotheApparentAgeEstimationAlgorithmTest,

                     # GENDER ESTIMATION ALGORITHMS
                     'levi_hassner_gender_estimation': CNNLeviHassnerGenderEstimationAlgorithmTest,
                     'rothe_gender_estimation': CNNRotheGenderEstimationAlgorithmTest,

                     # SKIN DETECTION ALGORITHMS
                     'simple_color_threshold_skin_detection': SimpleColorThresholdSkinDetectionAlgorithmTest,
                     'cheddad_2009_skin_detection': Cheddad2009SkinDetectionAlgorithmTest,
                     'bayes_lut_skin_detection': BayesLutSkinDetectionAlgorithmTest,
                     'bayes_lut_dempster_shafer_skin_detection': BayesLutDempsterShaferSkinDetectionAlgorithmTest,
                     'gaussian_distributed_skin_detection': GaussianDistributedSkinDetectionAlgorithmTest,
                     'chai_1999_skin_detection': Chai1999SkinDetectionAlgorithmTest,
                     'hsieh_2002_skin_detection': Hsieh2002SkinDetectionAlgorithmTest,
                     'kovak_2003_fl_skin_detection': Kovak2003FLSkinDetectionAlgorithmTest,
                     'kovak_2003_ud_skin_detection': Kovak2003UDSkinDetectionAlgorithmTest,
                     'soriano_2000_skin_detection': Soriano2000SkinDetectionAlgorithmTest,

                     # IMAGE CLASSIFICATION ALGORITHMS
                     'bow_svm_image_classification_linear_kernel': BowSVMImageClassificationLinearKernelAlgorithmTest,
                     'bow_svm_image_classification_poly3_kernel': BowSVMImageClassificationPoly5KernelAlgorithmTest,
                     'bow_svm_image_classification_rbf_kernel': BowSVMImageClassificationRBFKernelAlgorithmTest,

                     # TEXT CLASSIFICATION ALGORITHMS
                     'bow_logistic_regression_text_classification': BowLogisticRegressionTextClassificationAlgorithmTest,
                     'bow_svm_text_classification': BowSVMTextClassificationAlgorithmTest,
                     'bow_naive_bayes_text_classification': BowNaiveBayesTextClassificationAlgorithmTest,
                     'tfidf_logistic_regression_text_classification': TFIDFLogisticRegressionTextClassificationAlgorithmTest,
                     'tfidf_svm_text_classification': TFIDFSVMTextClassificationAlgorithmTest,
                     'tfidf_naive_bayes_text_classification': TFIDFNaiveBayesTextClassificationAlgorithmTest,
                     'hashing_logistic_regression_text_classification': HashingLogisticRegressionTextClassificationAlgorithmTest,
                     'hashing_svm_text_classification': HashingSVMTextClassificationAlgorithmTest,

                     # utilites
                     'imageblob': ImageTest,

                     'faceboundingboxcomparator': FaceBoundingBoxComparatorTest,
                     'agerange_comparator': AgeRangeComparatorTest,
                     'gender_comparator': GenderComparatorTest,

                     'boundingboxdrawer': BoundingboxDrawerTest,

                     'facedetectionreport': FaceDetectionReportTest,

                     }


def load_arguments():
    """


    :return: a list of arguments read from the config file
    """
    config_file_content = []

    if os.path.isfile(config_file):
        with open(config_file) as file:
            config_file_content = file.readlines()

    return config_file_content


def load_tests(loader, tests, pattern):
    modules_to_test = load_arguments()
    modules_to_test = [module.strip() for module in modules_to_test]

    if len(modules_to_test) == 1 and modules_to_test[0] == 'all':
        modules_to_test.pop()
        print("\nTesting ALL modules.\n")
    else:
        print("\nTesting {} modules.\n".format(len(modules_to_test)))

    suite = unittest.TestSuite()

    for id, module in available_modules.items():
        if len(modules_to_test) == 0 or id in modules_to_test:
            print("adding module {} to the test suite".format(id))
            tests = loader.loadTestsFromTestCase(module().__class__)
            suite.addTest(tests)
    print("\n======================================\n\n")

    return suite


def print_available_modules():
    print("Available modules are:\n")
    for id, module in available_modules.items():
        print("\t {}".format(id))

    print("\n\t all")


if __name__ == '__main__':
    modules_to_test = load_arguments()
    modules_to_test = [module.strip() for module in modules_to_test]
    if len(modules_to_test) == 0 or (len(modules_to_test) == 1 and modules_to_test[0] == "--help"):
        print("Usage: ./test.sh [module]")
        print_available_modules()
    else:
        unittest.main()

