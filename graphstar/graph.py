"""
	graphstar.graph
	~~~~~~~~~~~~~~~
	Cristian Cornea

	A simple bedirectional graph with A* and breadth-first pathfinding.

	Create nodes and connections. Connection costs will be calculated based
	on manhattan heuristic.
	Apply the graph with start and end note to bf or A* search, the result will
	be a list of node ids to take, to get to the goal node.
	Additional, add a heuristic to the search (for the total distance calculation)

	For more information see the examples and tests folder
"""

from .heuristic import manhatten


class Node(object):
	"""
	A node, representing a (x,y) 2DVector point in space
	"""
	def __init__(self):
		self.id = 0
		self.position = (0, 0)


class Connection(object):
	"""
	A connection in one direction between two nodes, and its costs.
	"""
	def __init__(self, from_node: Node, to_node: Node):
		self.from_node = from_node
		self.to_node = to_node
		self.cost = 0


class Graph:
	"""
	Base graph. Holds all nodes and connections.
	"""
	def __init__(self, digraph: bool=False):
		"""
		Constructor.

		:param digraph: bool  Does this graph support both directions?
		"""
		self.highest_id = 0
		self.__digraph = digraph
		self.__connections = {}
		self.__nodes = {}

	def node_by_id(self, node_id: int):
		"""
		Returns the node by its given id.

		:param node_id: int
		:return: Node|None
		"""
		if node_id in self.__nodes:
			return self.__nodes[node_id]
		return None

	def is_digraph(self):
		"""True if this graph supports both directions"""
		return self.__digraph

	def make_node(self, x: int, y: int):
		"""
		Takes two coordinates and creates a node.
		Gives the node a unique id and stores it.

		:param x: int
		:param y: int
		:return: Node
		"""
		p = (x, y)
		# Check if node does exsist on given position
		for k, v in self.__nodes.items():
			if v.position == p:
				return v

		# Create a node for the given position
		n = Node()
		n.id = self.highest_id
		self.highest_id += 1
		n.position = p
		self.__nodes[n.id] = n
		return n

	def make_connection(self, from_node: Node, to_node: Node):
		"""
		Creates a connection between two nodes.
		Calculates the edge cost with the manhattan heuristic.
		Stores the connection.

		:param from_node: int  Id of the start node
		:param to_node: int Id of the end noad
		:return: bool
		"""
		# Check if nodes are in graph
		if not self.nodes_in_graph(from_node, to_node):
			return False

		c = Connection(from_node, to_node)
		c.cost = manhatten(from_node.position, to_node.position)

		# If "from node" already has connections, append this one
		if from_node.id in self.__connections:
			# If "from node" has this connection already, do nothing
			for con in self.__connections[from_node.id]:
				if to_node.id == con.to_node.id:
					return False
			# If not add it
			self.__connections[from_node.id].append(c)
		# If "from node" has no connections, create first list
		else:
			self.__connections[from_node.id] = [c]

		return True

	def get_connections(self, node: Node):
		"""
		Returns all connections of a given node.

		:param node: Node  Id of the node
		:return: list
		"""
		if node.id in self.__connections:
			return self.__connections[node.id]
		# Node id not found in connections
		return []

	def node_on_position(self, pos: tuple):
		"""
		Searches for the given position in all nodes.

		:param pos: tuple  The position to test
		:return: bool
		"""
		for k, v in self.__nodes.items():
			if v.position == pos:
				return True
		return False

	def nodes_in_graph(self, *args):
		"""
		If there is a node on this position, return it

		:param args: nodes to test for
		:return: bool
		"""
		for n in args:
			if not self.node_on_position(n.position):
				return False
		return True

	def save_file(self):
		pass

	def load_file(self):
		pass
