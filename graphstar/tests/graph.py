import pytest
from graphstar import graph


@pytest.fixture(scope="function")
def g():
	return graph.Graph()


@pytest.fixture
def n():
	return graph.Node()


@pytest.fixture(scope="function")
def two_nodes(g):
	n1 = g.make_node(1, 1)
	n2 = g.make_node(2, 2)
	return n1, n2


def test_get_node_by_id(g):
	"""Test the node_by_id method"""
	n1 = g.make_node(1, 1)
	n2 = g.node_by_id(n1.id)
	assert n1 is n2 and n1.id == n2.id


def test_node_id_is_unique(g):
	"""Test incremental ids work"""
	for i in range(0, 10):
		n = g.make_node(i, i)
		assert n.id == i


def test_node_duplicate_not_allowed(g):
	"""Two nodes on the same position not allowed"""
	n1 = g.make_node(1, 1)
	n2 = g.node_by_id(n1.id)
	assert n1 is n2 and n1.id == n2.id


def test_connection_creation(g, two_nodes):
	"""Test the make_connection method"""
	n1, n2 = two_nodes
	c = g.make_connection(n1, n2)
	assert c is True


def test_get_connections(g, two_nodes):
	"""Test the get_connections method"""
	n1, n2 = two_nodes
	g.make_connection(n1, n2)

	clist = g.get_connections(n1)
	for c in clist:
		assert isinstance(c, graph.Connection)
		assert n1 is c.from_node and n2 is c.to_node


def test_connection_refuse(g, n):
	"""Connection with a node that is not in
	the Graph is not allowed"""
	# This node is in the graph, the other is not
	n1 = g.make_node(1, 1)
	c = g.make_connection(n, n1)
	assert c is False


def test_connection_costs(g):
	"""Test connection costs are assigned
	correctly (manhattan heuristic)"""
	n1 = g.make_node(1, 1)
	n2 = g.make_node(3, 3)
	g.make_connection(n1, n2)
	clist = g.get_connections(n1)

	for c in clist:
		assert c.cost == 4


def test_duplicate_connection_not_allowed(g, two_nodes):
	"""Duplicate connections in same direction
	are not allowed"""
	n1, n2 = two_nodes
	connected = g.make_connection(n1, n2)
	assert connected is True
	connect_again = g.make_connection(n1, n2)
	assert connect_again is False
