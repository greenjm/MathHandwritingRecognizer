import sys
import os
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib

CLF_FILENAME = '\optimalCLF.pkl'
CLF = None

def findOptimalSVM(data, target):
	"""
	Given a dataset and their appropriate targets,
	uses exhaustive grid search to determine the optimal
	SVM parameters for the set and saves the result to CLF_FILENAME
	"""
	scorer = svm.SVC()
	params = [{
				'kernel': ['rbf', 'linear', 'poly'],
				'gamma': ['auto', 1e-3, 1e-4, 1e-5, 1e-6],
				'C': [1, 10, 100, 1000],
				'probability': [True, False],
				'degree': [3, 4, 5]
			}]
	clf = GridSearchCV(scorer, params)
	clf.fit(data, target)

	cwd = os.path.dirname(os.path.realpath(__file__))

	joblib.dump(clf, cwd + CLF_FILENAME)

def classify(data):
	"""
	Given a dataset of the same form used for training
	in findOptimalSVM(), returns a classification array
	using the optimal SVM.
	NOTE: data should be an array of feature arrays, even for
	classifying one object e.g. [[1, 2, 3]]
	"""
	if CLF is None:
		cwd = os.path.dirname(os.path.realpath(__file__))
		global CLF
		CLF = joblib.load(cwd + CLF_FILENAME)
	return CLF.predict(data)