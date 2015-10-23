"""
	graphstar.search
	~~~~~~~~~~~~~~~~
	Cristian Cornea

	A simple bedirectional graph with A* and breadth-first pathfinding.

	Create nodes and connections. Connection costs will be calculated based
	on manhattan heuristic.
	Apply the graph with start and end note to bf or A* search, the result will
	be a list of node ids to take, to get to the goal node.
	Additional, add a heuristic to the search (for the total distance calculation)

	For more information see the examples and tests folder
"""

from collections import deque
from pqdict import pqdict
from .graph import Node, Connection, Graph
from .utils import clean_route_list


def a_star(graph: Graph, start: Node, goal: Node, heuristic):
	"""
	Standard A* search algorithm.

	:param graph: Graph A graph with all nodes and connections
	:param start: Node  Start node, where the search starts
	:param goal: Node   End node, the goal for the search
	:return: shortest_path: list|False     Either a list of node ids or false
	"""

	# Indexed priority queue
	queue = pqdict()

	# All visited connections
	visited_stack = {}
	# Add start node
	visited_stack[start] = True

	# The costs from start to a node
	cost_to_node = {}
	# Full costs from a node to goal
	full_costs = {}
	# All paths that have been taken
	shortest_path = []

	# Create a dummy for the start node
	dummy_connection = Connection(start, start)
	# Assign it to the queue so we can start
	queue[dummy_connection] = 0

	while queue:
		# Get next connection from top queue
		# and remove it (its a get + pop)
		connection = queue.pop()
		# Add the node to the shortest path
		# cause otherwise we would not be here
		shortest_path.append(connection)
		cost_to_node[connection.to_node] = connection.cost

		# We have found the target
		if connection.to_node.id == goal.id:
			# Remove all unneded paths and return
			# a sorted list
			return clean_route_list(shortest_path, goal.id)

		# Get all connected nodes
		next_connections = graph.get_connections(connection.to_node)
		# Iterate through all connected nodes
		# and calculate the costs and stuff
		for c in next_connections:
			# Calculate total costs from start to the goal node
			to_goal_cost = heuristic(goal.position, c.to_node.position)
			# Calculate costs from start to this node
			current_cost = cost_to_node[connection.to_node] + c.cost

			# Update lists and costs
			queue[c] = current_cost
			cost_to_node[c.to_node] = current_cost
			full_costs[c.to_node] = current_cost + to_goal_cost
			visited_stack[c.to_node] = True

	# Never found the target, so sad ...
	return False


def breadth_first(graph: Graph, start: Node, goal: Node):
	"""
	Standard breadth first search algorithm.

	:param graph: Graph A graph with all nodes and connections
	:param start: Node  Start node, where the search starts
	:param goal: Node   End node, the goal for the search
	:return: list|False Either a list of node ids or false
	"""

	queue = deque()
	route_stack = []

	visited_stack = {}
	visited_stack[start.id] = True

	dummy_connection = Connection(start.id, start.id)
	queue.append(dummy_connection)

	while queue:
		connection = queue.popleft()

		route_stack.append(connection)

		if connection.to_node == goal.id:
			return clean_route_list(route_stack, goal.id)

		next_connections = graph.get_connections(connection.to_node)

		for c in next_connections:
			if c.to_node not in visited_stack:
				queue.append(c)
				visited_stack[c.to_node] = True

	return False
