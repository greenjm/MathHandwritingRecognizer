import cv2
import numpy as np
from matplotlib import pyplot as plt

# read in image
img = cv2.imread('IMAG1480_1.jpg',0)
i2 = cv2.medianBlur(img, 3)


########################  Processing  ###############################

# adaptive Gaussian image thresholding
ag = cv2.adaptiveThreshold(i2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	cv2.THRESH_BINARY_INV, 9, 5)

########################  __________  ###############################

cv2.imshow('original', img)

cv2.imshow('current', ag)


cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('IMAG1480_12.jpg',ag)