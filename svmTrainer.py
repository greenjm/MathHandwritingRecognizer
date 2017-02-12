from __future__ import division
import sys
import os
import numpy as np
from os import listdir
import cv2
import symbolDict as di
import segmentation as seg
import extractFeatures as ef
import extractHOG as hog
import svm
from sklearn.externals import joblib

def runSVMTrainPipeline(absPath, numClfs, useHog):
	"""
	Given the absolute path of the training images folder (containing all of
	the subfolders) and the number of classifiers that should be trained,
	this function splits the dataset into numClfs sets, and runs the
	images through our pipeline up until the point an SVM has been trained
	on the set. If useHog is true, the HOG features will be extracted.
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
			#count = 0
			for j in range(0 + ((len(files)/numClfs)*i), min(((len(files)/numClfs)*(i+1)), ((len(files)/numClfs)*i) + 400)):
				if os.path.isfile(os.path.join(p, files[j])):
					img = cv2.imread(os.path.join(p, files[j]), 0)
					#extracted = ef.extractFeatures(seg.segmentImage(img))
					res, bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
					if useHog:
						extracted = hog.extractHOG(bw)
						print extracted
					else:
						extracted = ef.extractFeatures(bw)
					if len(extracted)==0:
						continue
					features.append(np.hstack(extracted))
					targets.append(key)
			sys.stdout.write(".")
		print "\n\nTraining: " + str(i+1)
		svm.findOptimalSVM(features, targets)
		print "\nTrained: " + str(i+1)

def getClassifierAccuracy(absPath, numClfs):
	cwd = os.path.dirname(os.path.realpath(__file__))
	i = 0
	filepath = os.path.join(cwd, str(i) + 'optimalCLF.pkl')
	symDict = di.getDict()
	features = []
	targets = np.array([])
	for key in symDict:
		p = os.path.join(absPath, str(symDict[key]))
		files = listdir(p)
		for j in range(0, len(files)):
			if os.path.isfile(os.path.join(p, files[j])):
				img = cv2.imread(os.path.join(p, files[j]), 0)
				#extracted = ef.extractFeatures(seg.segmentImage(img))
				res, bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
				extracted = ef.extractFeatures(bw)
				if len(extracted)==0:
					continue
				features.append(np.hstack(extracted))
				targets = np.append(targets, key)
		sys.stdout.write(".")
	for i in range(0, numClfs): #os.path.exists(filepath)
		CLF = joblib.load(filepath)
		preds = np.array(svm.classify(features, CLF))
		totalCorrect = np.sum(preds == targets)
		tot = len(preds)
		accuracy = totalCorrect / tot
		print "SVM: " + str(i) + " Accuracy: " + str(accuracy)
		#i = i + 1
		filepath = os.path.join(cwd, str(i) + 'optimalCLF.pkl')

def getVotingAccuracy(absPath, numClfs):
	cwd = os.path.dirname(os.path.realpath(__file__))
	i = 0
	filepath = os.path.join(cwd, str(i) + 'optimalCLF.pkl')
	symDict = di.getDict()
	features = []
	targets = np.array([])
	for key in symDict:
		p = os.path.join(absPath, str(symDict[key]))
		files = listdir(p)
		for j in range(0, len(files)):
			if os.path.isfile(os.path.join(p, files[j])):
				img = cv2.imread(os.path.join(p, files[j]), 0)
				res, bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
				extracted = ef.extractFeatures(bw)
				if len(extracted)==0:
					continue
				features.append(np.hstack(extracted))
				targets = np.append(targets, key)
		sys.stdout.write(".")
	print "\nVoting"
	preds = np.array(svm.voteClassify(features, numClfs))
	totalCorrect = np.sum(preds == targets)
	tot = len(preds)
	accuracy = totalCorrect / tot
	print "Voting Accuracy: " + str(accuracy)
