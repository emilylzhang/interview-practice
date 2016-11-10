from nose.tools import *
from maze import Maze
from graph import Graph


# Create new graph/test graph functionality.
def test_create_graph():
    g = Graph()
    g.insert_node(5)
    g.insert_node(6)
    g.insert_edge(5, 6, 4)

    # Test that looking for distance betwee edges works.
    dist = g.has_edge_dist(5, 6)
    assert_equal(dist, 4)
    # Test an exception.
    try:
        dist = g.has_edge_dist(5, 0)
    except LookupError:
        assert True
