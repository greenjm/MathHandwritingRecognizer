import Node as n

class Tree(object):

	def __init__(self, bboxes, imgArea):
		self.root = n.Node(bboxes, None)

	def getRoot(self):
		return self.root

	def addNode(self, pNode, bboxes):
		pNode.addChild(bboxes)

	def getTreeLevel(self, level):
		"""
		Returns all nodes of a certain depth in the tree,
		0 for root node, 1 for root's children, etc.
		"""
		nodes = [self.root]
		nextNodes = []
		while level > 0:
			for node in nodes:
				for child in node.getChildren():
					nextNodes.append(child)
			nodes = list(nextNodes)
			nextNodes = []
			level = level - 1
		return nodes

	def getLeafs(self, node):
		"""
		Returns all leaf nodes in depth-first-search order,
		starting at the given node
		"""
		leafs = []
		if node.isLeaf():
			return [node]

		for child in node.getChildren():
			for leaf in self.getLeafs(child):
				leafs.append(leaf)
		return leafs
