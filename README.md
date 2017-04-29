# Synopsis

The CvMlEval stands for **C**omputer **V**ision and **M**achine **L**earning **Eval**uator. This project is aimed to evaluate any kind of Computer Vision and/or Machine Learning algorithm against any kind of dataset.

It is entirely built in Python3.5, wrapping libs for standard algorithms like Face Detection from DLib or from OpenCV.
    
    
# Supported Algorithms

As of the current date (28/06/2016), the following algorithms are supported by the evaluator:


## Face Detection
| **Algorithm**                   | **Description**                                                                                   | **Status**  |
|---------------------------------|---------------------------------------------------------------------------------------------------|-------------|
| dlib_face_detection_algorithm   | Detects bounding boxes for faces by using `HOG` technique in a given picture.                     | Implemented |
| opencv_face_detection_algorithm | Detects bounding boxes for faces by using `Viola-Jones` Haar Cascade technique in a given picture | Implemented |
| neven_face_detection_algorithm  | Detects bounding boxes for faces by using Neven algorithm, extracted from Android O.S.            | Implemented |


## Age Estimation
| **Algorithm**                             | **Description**                                                                                          | **Status**  |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------|
| cnn_levi_hassner_age_estimation_algorithm | Estimates the age of a frontal face, based in Convolutional Neural Networks, work from Levi and Hassner. | Implemented |


## Gender Estimation
| **Algorithm**                                | **Description**                                                                                             | **Status**  |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------|
| cnn_levi_hassner_gender_estimation_algorithm | Estimates the gender of a frontal face, based in Convolutional Neural Networks, work from Levi and Hassner. | Implemented |


## Skin detection
|                    **Algorithm**                   | **Description**                                                                    | **Status**  |
|:--------------------------------------------------:|------------------------------------------------------------------------------------|-------------|
| cheddad_2009_skin_detection_algorithm              | Detects skin mask based on Cheddad static algorithm, from 2009                     | Implemented |
| kovak_2003_ud_skin_detection_algorithm             | Detects skin mask based on Kovak UD static algorithm, from 2003                    | Implemented |
| kovak_2003_fl_skin_detection_algorithm             | Detects skin mask based on Kovak FL static algorithm, from 2003                    | Implemented |
| hsieh_2002_skin_detection_algorithm                | Detects skin mask based on Hsieh static algorithm, from 2002                       | Implemented |
| soriano_2000_skin_detection_algorithm              | Detects skin mask based on Soriano static algorithm, from 2000                     | Implemented |
| chai_1999_skin_detection_algorithm                 | Detects skin mask based on Chai static algorithm, from 1999                        | Implemented |
| simple_color_threshold_skin_detection_algorithm    | Detects skin mask based on color threshold static algorithm.                       | Implemented |
| gaussian_distributed_skin_detection_algorithm      | Detects skin mask based on a gaussian distributed model, dynamic algorithm         | In progress |
| bayes_lut_dempster_shafer_skin_detection_algorithm | Detects skin mask based on bayes lut and dempster shafer method, dynamic algorithm | In progress |
| bayes_lut_skin_detection_algorithm                 | Detects skin mask based on Bayes Lut RGB method, dynamic algorithm                 | In progress |


## Image classification
|                     **Algorithm**                    | **Description**                                                                                | **Status**  |
|:----------------------------------------------------:|------------------------------------------------------------------------------------------------|-------------|
| bow_svm_image_classification_linear_kernel_algorithm | Classifies images by using the Bag Of Words with a linear kernel applied to SVM                | Implemented |
| bow_svm_image_classification_poly5_kernel_algorithm  | Classifies images by using the Bag Of Words with a polynomial kernel of grade 5 applied to SVM | Implemented |
| bow_svm_image_classification_rbf_kernel_algorithm    | Classifies images by using the Bag Of Words with a RBF kernel applied to SVM                   | Implemented |

## Text classification
|                         **Algorithm**                        | **Description**                                                             | **Status**  |
|:------------------------------------------------------------:|-----------------------------------------------------------------------------|-------------|
| bow_logistic_regression_text_classification_algorithm        | Classifies text by using Bag Of Words with a Logistic Regression classifier | Implemented |
| bow_naive_bayes_text_classification_algorithm                | Classifies text by using Bag Of Words with a Naive Bayes classifier         | Implemented |
| bow_support_vector_machine_text_classification_algorithm     | Classifies text by using Bag Of Words with a SVM classifier                 | Implemented |
| hashing_logistic_regression_text_classification_algorithm    | Classifies text by using Hashing with a Logistic Regression classifier      | Implemented |
| hashing_support_vector_machine_text_classification_algorithm | Classifies text by using Hashing with a SVM classifier                      | Implemented |
| tfidf_logistic_regression_text_classification_algorithm      | Classifies text by using TFIDF with a Logistic Regression classifier        | Implemented |
| tfidf_naive_bayes_text_classification_algorithm              | Classifies text by using TFIDF with a Naive Bayes classifier                | Implemented |
| tfidf_support_vector_machine_text_classification_algorithm   | Classifies text by using TFIDF with a SVM classifier                        | Implemented |

If you want to request a new algorithm support for the evaluator, do not hesitate in appending a milestone to the project.



# Supported Datasets


As of date (28/06/2016), the following datasets are supported by the evaluator:


| **Dataset**        | **Description**                       | **Status**  |
|--------------------|---------------------------------------|-------------|
| AFW                | Annotated Faces in the Wild dataset   | Implemented |
| ADIENCE_BRANCH     | Dataset from the University of Israel | Implemented |
| PRATHEEPAN         | Dataset for skin detection            | Implemented |
| EDU                | Dataset for image classification based on the pressence of a face | Implemented |



you can download the datasets from this [link](http://datasets.sockhost.net/).
In order to request access to the dataset webpage, issue an email to [us](mailto:ipazc@unileon.es).


# Available Evaluators


As of date (28/06/2016), the following evaluators are available:


| **Evaluator**     | **Description**                       | **Status**  |
|-------------------|---------------------------------------|-------------|
| face_detection    | Evaluator for face detection (for datasets with bounding boxes).         | Implemented |
| age_estimation    | Evaluator for age estimation.         | Implemented |
| gender_estimation | Evaluator for gender estimation.      | Implemented |
| simple_face_detection_evaluator | Evaluator for face detection (for datasets with and without faces).      | Implemented |
| skin_detection_evaluator | Evaluator for skin detection | Implemented |

# Installation

Check the [installation guide](INSTALL.md) file.

# API Reference

Check the wiki for more information.



# Tests

In order to test the solution, there is a set of unittests wrapped inside a test suite. The script `test.sh` allows you to perform the tests for the framework in different ways.
Since single or multiple modules can be tested, the list of available modules are shown if no arguments are specified: 

```bash
$ ./test.sh
```

You can append as many modules to test as you want, in any order:

```bash
$ ./test.sh dlibfacedetection afwdataset
```

or perform a full-solution test by using the `all` keyword:

```bash
$ ./test.sh all
```


# How to perform an evaluation

In order to perform an evaluation of a built-in algorithm, the `bin/*_evaluator.py` 
script must be invocated.
The "*" has to be replaced by the desired evaluator name. Check the [Available Evaluators section](#available-evaluators) 
to know the available evaluators names.

For example, an algorithm for face detection must replace the "*" by the face detection evaluator "face_detection". The result is `bin/face_detection_evaluator.py`.


You can receive information about its syntax by appending the -h flag:
```bash
$ python3 -m bin.face_detection_evaluator -h
```

To list available algorithms for the specified evaluator, you can use the -x flag:
```bash
$ python3 -m bin.face_detection_evaluator -x
```

To list supported datasets for the specified evaluator, you can use the -l flag:
```bash
$ python3 -m bin.face_detection_evaluator -l
```



## Example of usage
Suppose that this is the structure of a folder in your computer:
```
\
|__ AFW/
|   |
|   |__ ...
|   |__ gt_AFW.txt          // Metadata file
|
|__ CvMlEval/
```

Setting our working directory inside `CvMlEval/`, an usage example for
evaluating the DLIB Hog Face Detection algorithm with the AFW dataset could be:

```bash
$ python3 -m bin.face_detector_evaluator face_detection_dlib -d /AFW/ -m /AFW/gt_AFW.txt AFW
```


If a match_threshold value of 90% is desired (65% is the default if flag not set), it can be specified by appending the -t argument:
```bash
$ python3 -m bin.face_detector_evaluator face_detection_dlib -d /AFW/ -m /AFW/gt_AFW.txt AFW -t 0.9
```


All the results of the process will be saved in the folder `/AFW_dlib_hog/`, with the name of 'report.txt'. Note that the name of the result folder is constructed by the name of the dataset followed by the name of the applied algorithm.

Furthermore, dataset images can be drawn by the evaluator to represent the metadata. For example, the face detector evaluator is able to draw the
detected bounding boxes for each image. All you have to do is to append the `-s` flag to the evaluator invocation.

Also, the written images are going to be saved in the same folder than the report.


# Contributors

Any contribution to the project will be appreciated.


# License

This project is licensed under the [GNU GPLv3 license](LICENSE).