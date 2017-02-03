import cv2
import numpy as np
from matplotlib import pyplot as plt

# # read in image
# img = cv2.imread('test.png',0)

########################  Processing  ###############################

# adaptive Gaussian image thresholding
def segmentImage(img):
	# blur and apply Guassian adaptive threshold
	i2 = cv2.medianBlur(img, 3)
	ag = cv2.adaptiveThreshold(i2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)

	# close noise
	kernel = np.ones((2,2), np.uint8)
	opened = cv2.morphologyEx(ag, cv2.MORPH_OPEN, kernel)
	return opened

########################  __________  ###############################
# opened = segmentImage(img)
# cv2.imshow('original', img)

# cv2.imshow('current', opened)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite('IMAG1480_12.jpg', opened)


