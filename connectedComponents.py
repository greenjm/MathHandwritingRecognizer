import cv2
import numpy as np


class connectedComponents:
	def __init__(self, img):
		self.img = np.uint8(img)
		self.connectedComponents = None
		self.ccCount = 0
		self.symbols = None

	def findConnectedComponents(self):
		"""
		Finds a mask containing every connected component in the image
		"""
		output = cv2.connectedComponentsWithStats(self.img, 8, cv2.CV_32S)
		output1 = np.uint8(output[1])

		self.connectedComponents = output1
		self.ccCount = output[0]
		return self.connectedComponents

	def createComponentMasks(self):
		"""
		Returns an array of masks, where each mask contains exactly one
		of the connected components.
		"""
		labels = self.connectedComponents | self.findConnectedComponents()
		symbols = []
		for r in range(1,self.ccCount):
			symbols.append(labels)

		for r in range(1, self.ccCount):
			symbols[r-1] = np.where(labels != r, 0, labels)
			symbols[r-1] = np.where(symbols[r-1] == r, 1, symbols[r-1])

		self.symbols = symbols
		return self.symbols