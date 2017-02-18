import cv2
import numpy as np
import math

# read in image
img = cv2.imread('test.png',0)

########################  Processing  ###############################

# adaptive Gaussian image thresholding
def segmentImage(img):
	# blur and apply Guassian adaptive threshold
	i2 = cv2.medianBlur(img, 3)
	#ag = cv2.adaptiveThreshold(i2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)

	res, ag = cv2.threshold(i2, math.floor(0.6*np.mean(i2)), 255, cv2.THRESH_BINARY_INV)
	# close noise
	kernel = np.ones((2,2), np.uint8)
	opened = cv2.morphologyEx(ag, cv2.MORPH_OPEN, kernel)
	return opened
