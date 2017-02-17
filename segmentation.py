import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

# read in image
img = cv2.imread('test.png',0)

########################  Processing  ###############################

# adaptive Gaussian image thresholding
def segmentImage(img):
	# blur and apply Guassian adaptive threshold
	i2 = cv2.medianBlur(img, 3)
	#ag = cv2.adaptiveThreshold(i2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
	print np.mean(i2)
	print np.median(i2)
	print np.max(i2)
	res, ag = cv2.threshold(i2, math.floor(0.6*np.mean(i2)), 255, cv2.THRESH_BINARY_INV)
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


# #Connected components, symbols ends up with binary masks of each component. Not minimized BBox. Original size of image
# output = cv2.connectedComponentsWithStats(opened, 8, cv2.CV_32S)
# labels = output[1]
# symbols = []
# for r in range(output[0]):
# 	symbols.append(labels)
# for x in range(len(labels)):
# 	for y in range(len(labels[x])):
# 		for r in range(output[0]):
# 			if r == y:
# 				symbols[r][x][y] = 1
# 			else:
# 				symbols[r][x][y] = 0


# for r in range(output[0]):
# 	cv2.imshow(str(r), symbols[r])

# for x in range(len(symbols[3])):
# 	print(symbols[3][x])

# cv2.waitKey(0)
# cv2.destroyAllWindows()
