import Tree as t

def XYcut(tree):
	"""
	Given a tree with just a root node, performs an
	X-Y cut of the bounding boxes and
	returns a tree as the result
	"""

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

def cut(node, vertCut):
	# TODO