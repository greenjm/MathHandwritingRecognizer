import cv2
import numpy as np


class connectedComponents:
	def __init__(self, img):
		self.img = img
		self.connectedComponents = None
		self.symbols = None

	def findConnectedComponents(img):
		output = cv2.connectedComponentsWithStats(bw, 8, cv2.CV_32S)
		self.connectedComponents = output
		
		return output[1]

	def createComponentMasks(img):
		symbols = []
		for r in range(output[0]):
			symbols.append(labels)
		for x in range(len(labels)):
			for y in range(len(labels[x])):
				for r in range(output[0]):
					if r == y:
						symbols[r][x][y] = 1
					else:
						symbols[r][x][y] = 0
		self.symbols = symbols

		return symbols