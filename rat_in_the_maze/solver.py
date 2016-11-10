from maze import Maze
from graph import Graph


def create_graph_from_maze(maze):
    g = Graph()

    # insert start and goal position into graph
    g.insert_node(maze.start)
    g.insert_node(maze.goal)

    check_nodes = set([maze.start, maze.goal])

    # add edges in graph
    while True:
        if not check_nodes:
            break
        new_nodes = edge_to_neighbors(g, check_nodes.pop(), maze)
        check_nodes.update(new_nodes)


def edge_to_neighbors(g, pos, maze):
    x, y = pos[0], pos[1]
    new_nodes = set()

    # add western neighbor
    westx = x + 1
    while westx < maze.size and not maze.has_wall(pos, 'W'):
        westx += 1
    new_node = (westx, y)
    if westx < maze.size:
        if not g.has_node(new_node):
            g.insert_node(new_node)
            new_nodes.add(new_node)
        g.insert_edge(pos, new_node, westx - x)

    # add eastern neighbor
    eastx = x - 1
    while eastx >= 0 and not maze.has_wall(pos, 'E'):
        eastx -= 1
    new_node = (eastx, y)
    if eastx >= 0:
        if not g.has_node(new_node):
            g.insert_node(new_node)
            new_nodes.add(new_node)
        g.insert_edge(pos, new_node, x - eastx)

    # add northern neighbor
    northy = y + 1
    while northy < maze.size and not maze.has_wall(pos, 'N'):
        northy += 1
    new_node = (x, northy)
    if northy < maze.size:
        if not g.has_node(new_node):
            g.insert_node(new_node)
            new_nodes.add(new_node)
        g.insert_edge(pos, new_node, northy - y)

    # add southern neighbor
    southy = y - 1
    while southy >= 0 and not maze.has_wall(pos, 'S'):
        southy -= 1
    new_node = (x, southy)
    if southy >= 0:
        if not g.has_node(new_node):
            g.insert_node(new_node)
            new_nodes.add(new_node)
        g.insert_edge(pos, new_node, y - southy)

    return new_nodes
