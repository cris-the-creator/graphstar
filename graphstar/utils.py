"""
	graphstar.utils
	~~~~~~~~~~~~~~~
	Cristian Cornea

	A simple bedirectional graph with A* and breadth-first pathfinding.

	Utils are either used by the search algorithm, or when needed :)
	Pretty self explainatory (I hope)

	For more information see the examples and tests folder
"""


def smooth_path(p):
	# If the path is only two nodes long, then
	# we can’t smooth it, so return
	if len(p) == 2:
		return p

	# Compile an output path
	output = [p[0]]

	# Keep track of where we are in the input path
	# We start at 2, because we assume two adjacent
	# nodes will pass the ray cast
	i = 2
	# Loop until we find the last item in the input
	while i < len(p)-1:
		# Do the ray cast
		if not ray_clear(output[len(output)-1], p[i]):
			# The ray text failed, add the last node that
			# passed to the output list
			output += p[i-1]
		# Consider the next node
		i += 1

	# We’ve reached the end of the input path, add the
	# end node to the output and return it
	output += p[len(p)-1]
	return output


def clean_route_list(route_stack: list, goal_node_id: int):
	"""
	Creates an ordered route list from start to finish
	with all node ids needed to traverse to the goal.

	:param route_stack:     All routes found until goal
	:param goal_node: int   ID of the goal node
	:return: list           A ordered list from start to goal
	"""
	r = []
	next_node = goal_node_id
	reversed_stack = reversed(route_stack)
	for c in reversed_stack:
		if c.to_node.id == next_node:
			r.append(c.to_node.id)
			r.append(c.from_node.id)
			next_node = c.from_node.id

	return list(set(r))
