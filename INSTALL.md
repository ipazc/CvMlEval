# Installation Guide

## For Ubuntu/Debian

### Install dependencies

```bash
$ sudo apt-get install -y build-essential cmake git python3 python3-skimage wget unzip pkg-config
```

### Make a structure for the project

Create a folder structure like the following:

```bash
\                            # Root folder (any)
|
|___datasets/                # Datasets folder
```

From the selected root folder, which we call `\` from now on, clone the last stable version of the repository:
```bash
$ git clone -b stable https://gitlab.com/varpsec/CvMlEval.git 
```

The expected structure is now:
```bash
\                            # Root folder (any)
|
|___CvMlEval                 # Computer Vision and Machine Learning Evaluator
|___datasets/                # Datasets folder
```

### Build support for DLib HOG Face Detection algorithm

Download, compile and install the version 18.18 of the DLib library (further versions should also work) **with Python3 support**:
```bash
$ cd /tmp/ 
$ wget http://dlib.net/files/dlib-18.18.tar.bz2
$ tar xvjf dlib-18.18.tar.bz2
$ cd dlib-18.18
$ sudo python3 setup.py install
```

### Build support for Neven Google-Android Face Detection algorithm

Download, compile and install the Neven algorithm project:
```bash
$ cd /tmp/
$ git clone https://gitlab.com/varpsec/neven.git
$ cd neven
$ make
$ sudo make install
```

### Build support for OpenCV3 Viola-Jones Face Detection algorithm

Install dependencies for OpenCV

#### Ubuntu 14.04
```bash
$ sudo apt-get -y install libopencv-dev libgtk2.0-dev pkg-config python-dev python-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff4-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev libqt4-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils
```

#### Ubuntu 15.04+
```bash
$ apt-get -y install libopencv-dev libgtk2.0-dev pkg-config python-dev python-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff5-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine2-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev libqt4-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils
```


Get OpenCV3 from the [http://opencv.org/](http://opencv.org/) page:
```bash
$ cd /tmp/
$ wget https://github.com/Itseez/opencv/archive/3.1.0.zip
$ unzip 3.1.0.zip && cd opencv-3.1.0
$ mkdir build && cd build
$ (cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=OFF -DWITH_IPP=OFF -D CMAKE_BUILD_TYPE=RELEASE -D WITH_CUDA=OFF -D PYTHON_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") -D PYTHON_EXECUTABLE=$(which python3) -D PYTHON_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") ..)
$ make -j $(nproc)
$ sudo make install
```

# Test framework
In order to know if all the modules are built successfully, the CvMLEval test suite can be executed. Instructions in how to do this can be seen in the main readme [tests section](README.md#tests).
