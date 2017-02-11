import os
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib

CLF_FILENAME = 'optimalCLF.pkl'
CLF = None

def findOptimalSVM(data, target):
	"""
	Given a dataset and their appropriate targets,
	uses exhaustive grid search to determine the optimal
	SVM parameters for the set and saves the result to CLF_FILENAME
	"""
	scorer = svm.SVC()
	params = [{
				'kernel': ['rbf', 'poly'],
				'gamma': ['auto', 1e-3, 1e-4, 1e-5],
				'C': [1, 10, 100],
				'probability': [True, False],
				'degree': [3, 4]
			}]
	clf = GridSearchCV(scorer, params)
	clf.fit(data, target)

	cwd = os.path.dirname(os.path.realpath(__file__))
	i = 0
	filepath = cwd + '\\' + str(i) + CLF_FILENAME
	while os.path.exists(filepath):
		print str(i)
		i = i + 1
		filepath = cwd + '\\' + str(i) + CLF_FILENAME

	joblib.dump(clf, cwd + CLF_FILENAME)

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