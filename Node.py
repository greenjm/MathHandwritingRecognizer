class Node(object):
	
	def __init__(self, bboxes, parent):
		self.bboxes = bboxes
		self.parent = parent
		self.children = []

	def getBBoxes(self):
		return self.bboxes

	def getParent(self):
		return self.parent

	def getChildren(self):
		return self.children

	def isRoot(self):
		return self.parent is None

	def isLeaf(self):
		return len(self.children) == 0

	def addChild(self, bboxes):
		self.children.append(Node(bboxes, self))