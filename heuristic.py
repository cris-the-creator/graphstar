"""
	graphstar.heuristic
	~~~~~~~~~~~~~~~~~~
	Cristian Cornea

	A simple bedirectional graph with A* and breadth-first pathfinding.

	A few simple heuristics. By default the graph connection costs between
	two points are calculated based on the manhatten heuristic.

	Others can be used with the search method, for the total distance
	calculation.

	For more information see the examples and tests folder
"""


import math


def manhatten(a: tuple, b: tuple):
	"""
	Manhattan distance
	The standard heuristic for a square grid.

	:param a: tuple  Start node position
	:param b: tuple  End node position
	:return: float
	"""
	ax, ay, bx, by = a[0], a[1], b[0], b[1]
	dx = abs(ax - bx)
	dy = abs(ay - by)
	return dx + dy


def diagonal(a: tuple, b:tuple):
	"""
	Diagonal distance
	On a square grid that allows 8 directions of movement.

	:param a: tuple  Start node position
	:param b: tuple  End node position
	:return: float
	"""
	ax, ay, bx, by = a[0], a[1], b[0], b[1]
	dx = abs(ax - bx)
	dy = abs(ay - by)
	return (dx + dy) * min(dx, dy)


def euclidean(a: tuple, b: tuple):
	"""
	Euclidean distance
	If your units can move at any angle (instead of grid directions),
	then you should probably use a straight line distance

	:param a: tuple  Start node position
	:param b: tuple  End node position
	:return: float
	"""
	ax, ay, bx, by = a[0], a[1], b[0], b[1]
	dx = abs(ax - bx)
	dy = abs(ay - by)
	return math.sqrt(dx * dx + dy * dy)
