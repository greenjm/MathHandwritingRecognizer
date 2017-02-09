import os
from os import listdir
import cv2
import symbolDict as di
import segmentation as seg
import extractFeatures as ef
import svm


def runSVMTrainPipeline(absPath, numClfs):
	"""
	Given the absolute path of the training images folder (containing all of
	the subfolders) and the number of classifiers that should be trained,
	this function splits the dataset into numClfs sets, and runs the
	images through our pipeline up until the point an SVM has been trained
	on the set
	"""
	if not os.path.isdir(absPath):
		print "Path not found: " + absPath
		return

	symDict = di.getDict()

	for i in range(0, numClfs):
		features = []
		targets = []

		for key in symDict:
			p = os.path.join(absPath, str(symDict[key]))
			if not os.path.isdir(p):
				print "Path not found: " + p
				return
			files = listdir(p)
			for j in range(0 + ((len(files)/numClfs)*i), ((len(files)/numClfs)*(i+1))):
				if os.path.isfile(os.path.join(p, files[j])):
					img = cv2.imread(os.path.join(p, files[j]), 0)
					extracted = ef.extractFeatures(seg.segmentImage(img))
					features.append(extracted)
					targets.append(key)
			print "."
		print "\nTraining: " + str(i+1)
		svm.findOptimalSVM(features, targets)
		print "\nTrained: " + str(i+1)
