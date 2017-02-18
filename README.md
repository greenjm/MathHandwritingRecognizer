# MathHandwritingRecognizer

## Installation

If you have Python 2.7 installed, pull the Py27 branch. Pull the master branch for the Python 3 version.
This project relies on several Python packages: OpenCV, Numpy, SciPy, and Scikit-learn
  Scikit-learn relies on Numpy and SciPy. We can try installing these two with pip with the following commands:
    `pip install numpy` and `pip install scipy`
  Then, install the latest version of scikit with `pip install -U scikit-learn`
  We ran into issues with this method, and had to install Numpy and SciPy using pre-built Windows binaries from [http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
  Download the latest Numpy and SciPy packages based on Python version ![Numpy](https://github.com/greenjm/MathHandwritingRecognizer/blob/master/images/numpy.PNG "Numpy package")![SciPy](https://github.com/greenjm/MathHandwritingRecognizer/blob/master/images/scipy.PNG "SciPy package")
  
  Install each with `pip install path/to/whl-file.whl`
  For Python 2.7, OpenCV can be installed by following the instructions at [http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html)
  For all versions, you can install a whl file from the same place as Numpy and SciPy ![OpenCV](https://github.com/greenjm/MathHandwritingRecognizer/blob/master/images/opencv.PNG "OpenCV package")
  
  Install with `pip install path/to/whl-file.whl`
After completing these steps, you should be ready to run the project.

## Dataset and Training

- If you would like to run the training yourself, you can install the dataset from either [https://www.kaggle.com/xainano/handwrittenmathsymbols](https://www.kaggle.com/xainano/handwrittenmathsymbols) or [https://drive.google.com/file/d/0B-uMaCuZp5_eVThtT2EwRVFGU1U/view?usp=sharing](https://drive.google.com/file/d/0B-uMaCuZp5_eVThtT2EwRVFGU1U/view?usp=sharing)
- runTraining.py contains the calls necessary to train the classifiers and test accuracy.
- Replace each "FILEPATH" in runTraining.py with the path to the dataset folder that you downloaded above.
- symbolDict.py contains a method called getAccuracies. This has been filled with the accuracies discovered during our testing. This dictionary must contain each classifier's accuracy in order for the getVotingAccuracy() call to work.
- To skip training and move straight to classifying real images, download the classifiers we trained from [https://drive.google.com/file/d/0B-uMaCuZp5_eeHRhZjJjRUxQbGc/view?usp=sharing](https://drive.google.com/file/d/0B-uMaCuZp5_eeHRhZjJjRUxQbGc/view?usp=sharing) and extract them into the project folder.
Once you have the trained classifiers, and the accuracies have been filled in to 

## Run the program

There are two options for executing the program. If you have a webcam installed, you can take an image using the webcam and the program will classify the image. Alternatively, you can provide a path to an existing image to have it classified.

- Open a terminal and navigate to the project folder
- To use a webcam, run `python main.py`
..-Your webcam should launch in a new window. Press enter to take an image of an expression, then follow the printed instructions to run the program
- To use an existing image, run `python main.py path/to/image` and follow the instructions to run the program

## Explanation of other files

**boundingBox.py:**
This file contains all of the functions necessary to find both the raw bounding boxes and the resized bounding boxes. Raw bounding boxes are used in grammar, and the resized boxes are used for classification.

**connectedComponents.py:**
This file contains a class with all functions related to connected components. There are functions for finding the connected components mask, and for gathering an array of masks, with each containing exactly one component.

**extractFeatures.py:**
Outdated file. Returns a feature vector with circularity, elongation, and principal axes. This file is no longer used during program execution.

**extractHOG.py:**
Contains the current functions we use for feature extraction. An image is passed to extractHOG(), the image is deskewed, and a feature vector is returned.

**main.py:**
The program execution script. Connects all components in the pipeline currently used for classification and grammar parsing.

**Node.py and Tree.py:**
Custom classes used to build a tree during X-Y-cutting.

**segmentation.py:**
Contains one function, segmentImage(), that applies a median blur and other thresholding to convert a grayscale image to a binary mask.

**svm.py:**
Contains all functions necessary for SVM training and classification. SVM training uses grid search to find an optimal classifier given a set of feature arrays, then saves the classifier to a file. Vote classification uses the accuracies determined earlier to classify a set of feature arrays.

**svmTrainer.py:**
Contains functions to train SVMs and find SVM classifier accuracies. Use runTrainer.py for example calls to this file's functions.

**symbolDict.py:**
Contains two functions that return dictionaries. getDict() returns a dictionary that maps a SVM classification to the symbol that classification represents. getAccuracies() returns a dictionary that maps each SVM's id (denoted by the filename) to the accuracy that SVM had on the validation set.

**xycut.py:**
This file is used for the first step of grammar parsing. XYcut() takes an array of all bounding boxes in the image, and returns a tree built with Tree.py that informs a parser of the ordering of elements in the image.
