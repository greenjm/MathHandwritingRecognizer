import math

class node:
	def __init__(self, centroid, possibilities = None, probabillities = None, connections=None):
		self.centroid = centroid
		self.possible = possibilities | []
		self.p = probabillities | []
		self.c = connections | [[], [], [], [], [], [], [], []]

	def getDistanceVector(self, node):
		x = self.centroid[0] - node.centroid[0]
		y = self.centroid[1] - node.centroid[1]

	def E(self, n = None):
		if n is not None:
			self.c[0].append(n)
			n.c[4].append(self)
		return self.c[0]
	def NE(self, n = None):
		if n is not None:
			self.c[1].append(n)
			n.c[5].append(self)
		return self.c[1]
	def N(self, n = None):
		if n is not None:
			self.c[2].append(n)
			n.c[6].append(self)
		return self.c[2]
	def NW(self, n = None):
		if n is not None:
			self.c[3].append(n)
			n.c[7].append(self)
		return self.c[3]
	def W(self, n = None):
		if n is not None:
			self.c[4].append(n)
			n.c[0].append(self)
		return self.c[4]
	def SW(self, n = None):
		if n is not None:
			self.c[5].append(n)
			n.c[1].append(self)
		return self.c[5]
	def S(self, n = None):
		if n is not None:
			self.c[6].append(n)
			n.c[2].append(self)
		return self.c[6]
	def SE(self, n = None):
		if n is not None:
			self.c[7].append(n)
			n.c[3].append(self)
		return self.c[7]

class syntaxMap:
	def __init__(self, root, bbox):
		self.nodes = [root]
		self.bboxs = [bbox]
		self.root = root
	
	def insert(self, new): # insert a node into the graph
		if self.root == None:
			self.root = new

		temp = self.root
		for n in self.nodes:
			dv = n.getDistanceVector(new)
			m = math.sqrt(math.pow(dv[0], 2) + math.pow(dv[1], 2))
			u = [dv[0]/m, dv[1]/m]
			m = math.sqrt(math.pow(u[0], 2) + math.pow(u[1], 2))

			# get angle
			theta = math.atan2(dv[0],dv[1])

			# connect fully at best angle to other nodes
			if theta >0:
				if math.abs(theta - math.pi) < math.pi/16:
					n.W(new)
				elif math.abs(theta - 3/4*math.pi) < math.pi/16:
					n.NW(new)
				elif math.abs(theta - 1/2*math.pi) < math.pi/16:
					n.N(new)
				elif math.abs(theta - 1/4*math.pi) < math.pi/16:
					n.NE(new)
				elif math.abs(theta) < math.pi/16:
					n.E(new)
			else:
				theta = -1*theta;
				if math.abs(theta - math.pi) < math.pi/16:
					n.W(new)
				elif math.abs(theta - 3/4*math.pi) < math.pi/16:
					n.SW(new)
				elif math.abs(theta - 1/2*math.pi) < math.pi/16:
					n.S(new)
				elif math.abs(theta - 1/4*math.pi) < math.pi/16:
					n.SE(new)
				elif math.abs(theta) < math.pi/16:
					n.E(new)

	def optimizeAngleConnections(self): # make all nodes have single connections at each angle
		for n in self.nodes:
			for a in range(8):
				m = []
				for c in n.c[a]:
					temp = n.getDistanceVector(c)
					m.append( math.sqrt(math.pow(temp[0], 2) + math.pow(temp[1], 2)) )
				m = m.index(min(m))
				n.c[a] = [n.c[a][m]]

	def dijkstra(self, root): # perform a single step in dijkstra's algorithm
		Q = []
		dist = self.nodes[:]
		prev = self.nodes[:]
		for v in range(len(self.nodes)):
			dist[v] = float('infinity')
			prev[v] = None
			Q.append({d:dist[v], prev:prev[v]})
		Q[self.nodes.index(root)].dist = 0

		while len(Q) > 0:
			ui = min(dist)
			u = Q[ui]
			del Q[ui]

			for n in u:
				# find min dist/max prob of transition between graph nodes
				alt = u.dist + cost(self.nodes[ui], n)
				if alt < u.dist:
					u.dist = alt
					u.prev = n

	def findOptimal(self):
		best = 0
		for n in self.nodes:
