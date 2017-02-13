import Tree as t

def XYcut(bboxes):
	"""
	Given a tree with just a root node, performs an
	X-Y cut of the bounding boxes and
	returns a tree as the result
	"""
	tree = t.Tree(bboxes)
	vChange = True
	hChange = True
	level = 0

	while vChange or hChange:
		vChange = False
		hChange = False
		nodes = tree.getTreeLevel(level)
		for node in nodes:
			changed = cut(node, True)
			if changed:
				vChange = True
		if vChange:
			level = level + 1
		nodes = tree.getTreeLevel(level)
		for node in nodes:
			changed = cut(node, False)
			if changed:
				hChange = True
		if hChange:
			level = level + 1

	return tree

def cut(tree, node, vertCut):
	"""
	Given a node within a tree, preform either
	vertical or horizontal cutting based on vertCut.
	New nodes will be added to the tree if changes made,
	and a boolean is returned if new nodes were added.
	"""
	if vertCut:
		minX = getMin(node, 0)
		maxX = getMax(node, 2)
		for i in range(minX, maxX):
			


def getMin(node, bboxIndex):
	"""
	Returns the minimum value of the given bboxIndex
	in all of the nodes bounding boxes
	"""
	bboxes = node.getBBoxes()
	minimum = bboxes[0][bboxIndex]
	for i in range(1, len(bboxes)):
		minimum = min(minimum, bboxes[i][bboxIndex])
	return minimum

def getMax(node, bboxIndex):
	"""
	Returns the maximum value of the given bboxIndex
	in all of the nodes bounding boxes
	"""
	bboxes = node.getBBoxes()
	maximum = bboxes[0][bboxIndex]
	for i in range(1, len(bboxes)):
		maximum = max(maximum, bboxes[i][bboxIndex])
	return maximum