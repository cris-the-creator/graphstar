"""
Graph for the tests:

n1 -> n2 START

n2 -> n3
n2 -> n4

n4 -> n5

n3 -> n6
n3 -> n7

n7 -> n8 GOAL

Fastest way from n2 to n8: n2->n3->n7->n8
"""


import pytest
from graphstar import search, heuristic, graph


@pytest.fixture(scope="module")
def g():
	g = graph.Graph(digraph=False)

	# Nodes
	n1 = g.make_node(2, 8)
	n2 = g.make_node(3, 7)
	n3 = g.make_node(2, 5)
	n4 = g.make_node(8, 7)
	n5 = g.make_node(10, 9)
	n6 = g.make_node(1, 4)
	n7 = g.make_node(2, 3)
	n8 = g.make_node(1, 1)

	# Connect them
	g.make_connection(n1, n2)
	g.make_connection(n2, n3)
	g.make_connection(n2, n4)
	g.make_connection(n4, n5)
	g.make_connection(n3, n6)
	g.make_connection(n3, n7)
	g.make_connection(n7, n8)

	return g


@pytest.fixture(scope="module")
def start_node(g):
	return g.node_by_id(1)


@pytest.fixture(scope="module")
def end_node(g):
	return g.node_by_id(7)


@pytest.fixture
def n():
	return graph.Node()


@pytest.fixture(scope="module")
def h():
	return heuristic.euclidean


def test_a_search_end_node_not_in_graph(g, start_node, n, h):
	route = search.a_star(g, start_node, n, h)
	assert route is False


def test_a_search_returns_route(g, start_node, end_node, h):
	route = search.a_star(g, start_node, end_node, h)
	# Fastest way from n2(id 1) to n8(id 7): n2->n3->n7->n8
	assert route == [1, 2, 6, 7]


def test_bf_search_end_node_not_in_graph():
	pass