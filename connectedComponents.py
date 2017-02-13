import cv2
import numpy as np


class connectedComponents:
	def __init__(self, img):
		self.img = img
		self.connectedComponents = None
		self.ccCount = 0
		self.symbols = None

	def findConnectedComponents(self):
		output = cv2.connectedComponentsWithStats(self.img, 8, cv2.CV_32S)
		self.connectedComponents = output[1]
		self.ccCount = output[0]
		return self.connectedComponents

	def createComponentMasks(self):
		labels = self.connectedComponents | self.findConnectedComponents()
		symbols = []
		for r in range(self.ccCount):
			symbols.append(labels)
		for x in range(len(labels)):
			for y in range(len(labels[x])):
				for r in range(self.ccCount):
					if r == y:
						symbols[r][x][y] = 1
					else:
						symbols[r][x][y] = 0
		self.symbols = symbols
		return self.symbols