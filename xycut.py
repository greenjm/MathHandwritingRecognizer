import Tree as t

def XYcut(bboxes):
	"""
	Given a list of bounding boxes, performs an
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
			vThreshold = getVThreshold(node.getBBoxes())
			changed = cut(tree, node, True, vThreshold)
			if changed:
				vChange = True
		if vChange:
			level = level + 1
		nodes = tree.getTreeLevel(level)
		for node in nodes:
			hThreshold = getHThreshold(node.getBBoxes())
			changed = cut(tree, node, False, hThreshold)
			if changed:
				hChange = True
		if hChange:
			level = level + 1

	return tree

def cut(tree, node, vertCut, threshold):
	"""
	Given a node within a tree, preform either
	vertical or horizontal cutting based on vertCut.
	New nodes will be added to the tree if changes made,
	and a boolean is returned if new nodes were added.
	"""
	bboxes = node.getBBoxes()
	gapStart = -1
	gapEnd = -1
	changeFlag = False
	if vertCut:
		minX = getMin(node, 0)
		maxX = getMax(node, 2)
		for i in range(minX, maxX):
			if gapStart==-1 and not vertIntersect(i, bboxes):
				gapStart = i
			elif gapStart!=-1 and vertIntersect(i, bboxes):
				gapEnd = i-1
			if gapStart!=-1 and gapEnd!=-1:
				if (gapEnd-gapStart) >= threshold:
					changeFlag = True
					bboxes = makeVertCut(tree, node, bboxes, (gapStart+gapEnd)/2)
				gapStart = -1
				gapEnd = -1
		if changeFlag:
			tree.addNode(node, bboxes)
	else:
		minY = getMin(node, 1)
		maxY = getMax(node, 3)
		for i in range(minY, maxY):
			if gapStart==-1 and not horizIntersect(i, bboxes):
				gapStart = i
			elif gapStart!=-1 and horizIntersect(i, bboxes):
				gapEnd = i
			if gapStart!=-1 and gapEnd!=-1:
				if (gapEnd-gapStart) >= threshold:
					changeFlag = True
					bboxes = makeHorizCut(tree, node, bboxes, (gapStart+gapEnd)/2)
				gapStart = -1
				gapEnd = -1
		if changeFlag:
			tree.addNode(node, bboxes)
	return changeFlag

def getVThreshold(bboxes):
	avg = 0
	for box in bboxes:
		avg = avg + (box[2] - box[0])
	return 0.5 * (avg / len(bboxes))

def getHThreshold(bboxes):
	avg = 0
	for box in bboxes:
		avg = avg + (box[3] - box[1])
	return 0.5 * (avg / len(bboxes))


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

def vertIntersect(i, bboxes):
	"""
	Returns true if a vertical line at i would
	intersect any bounding boxes in the bboxes
	array.
	"""
	for box in bboxes:
		if box[0] <= i and box[2] >= i:
			return True
	return False

def horizIntersect(i, bboxes):
	"""
	Returns true if a horizontal line at i would
	intersect any bounding boxes in the bboxes
	array.
	"""
	for box in bboxes:
		if box[1] <= i and box[3] >= i:
			return True
	return False

def makeVertCut(tree, node, bboxes, index):
	"""
	Adds a new node to the tree containing the bboxes
	to the left of the index. Returns an array containing
	all other bboxes
	"""
	leftBoxes = []
	rightBoxes = []
	for box in bboxes:
		if box[2] <= index:
			# maxX is left of index
			leftBoxes.append(box)
		else:
			rightBoxes.append(box)
	tree.addNode(node, leftBoxes)
	return rightBoxes

def makeHorizCut(tree, node, bboxes, index):
	"""
	Adds a new node to the tree containing the bboxes
	above the index. Returns an array containing
	all other bboxes
	"""
	aboveBoxes = []
	belowBoxes = []
	for box in bboxes:
		if box[3] <= index:
			# maxY is above index
			aboveBoxes.append(box)
		else:
			belowBoxes.append(box)
	tree.addNode(node, aboveBoxes)
	return belowBoxes