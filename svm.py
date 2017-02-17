import sys
import os
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
import symbolDict as di

CLF_FILENAME = 'optimalCLF.pkl'
CLF = None

def findOptimalSVM(data, target, fileId):
	"""
	Given a dataset and their appropriate targets,
	uses exhaustive grid search to determine the optimal
	SVM parameters for the set and saves the result to CLF_FILENAME
	"""
	scorer = svm.SVC()
	params = [{
				'kernel': ['rbf'],
				'gamma': ['auto', 1e-3, 1e-4, 1e-5, 1e-6],
				'C': [1, 10, 100],
				'probability': [True]
			}]
	clf = GridSearchCV(scorer, params)
	clf.fit(data, target)

	cwd = os.path.dirname(os.path.realpath(__file__))
	#i = 0
	filepath = os.path.join(cwd, str(fileId) + CLF_FILENAME)
	#while os.path.exists(filepath):
	#	i = i + 1
	#	filepath = os.path.join(cwd, str(i) + CLF_FILENAME)

	joblib.dump(clf, filepath)

def classify(data, clf):
	"""
	Given a dataset of the same form used for training
	in findOptimalSVM() and a classifier, returns a classification
	array using the optimal SVM.
	NOTE: data should be an array of feature arrays, even for
	classifying one object e.g. [[1, 2, 3]]
	"""
	#global CLF
	#if CLF is None:
	#	cwd = os.path.dirname(os.path.realpath(__file__))
	#	CLF = joblib.load(cwd + CLF_FILENAME)
	return clf.predict(data)

def voteClassify(data, numClfs, start):
	"""
	Use the numClfs to classify the data through voting
	e.g. numClfs will use 0optimalCLF.pkl, 1, and 2.
	"""
	clfs = []
	preds = []
	res = []
	accuracies = di.getAccuracies()
	cwd = os.path.dirname(os.path.realpath(__file__))
	for i in range(start, start+numClfs):
		filepath = os.path.join(cwd, str(i) + CLF_FILENAME)
		clfs.append(joblib.load(filepath))
	#for clf in clfs:
	#	preds.append(clf.predict(data))
	for i in range(0, len(data)):
		votes = dict()
		for j in range(start, start+numClfs):
			vote = clfs[j-start].predict([data[i]])[0]
			votes[vote] = votes.get(vote, 0) + (accuracies[j] * 1)
		res.append(max(votes, key = lambda x: votes.get(x)))
		#sys.stdout.write(".")
	return res