# Nodes cannot be deleted once they are added to the graph.
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}         # node : list of (node, dist to node)

    def insert_node(self, val):
        self.nodes.add(val)

    def has_node(self, val):
        return val in self.nodes

    # Add a directed edge between from_node and to_node.
    def insert_edge(self, from_node, to_node, distance):
        if distance < 1:
            raise ValueError("Edges must have a distance of at least 1.")
            return
        if not (from_node in self.nodes and to_node in self.nodes):
            print("Tried to add edge between nonexistent nodes.")
            return
        if from_node not in self.edges:
            self.edges[from_node] = [(to_node, distance)]
        else:
            self.edges[from_node].append((to_node, distance))

    # Checks if there exists an edge from from_node to to_node. If so,
    # return the distance of that node. If there is no edge between these two
    # nodes, return 0. O(N) time complexity where N is the max number of edges
    # that a node in the graph has. TODO: Can we do better? (using sets?)
    def has_edge_dist(self, from_node, to_node):
        if not (from_node in self.nodes and to_node in self.nodes):
            raise LookupError("Tried to check for edge b/n nonexistent nodes.")
            return
        if from_node not in self.edges:
            return 0
        for node, distance in self.edges[from_node]:
            if node == to_node:
                return distance
        print("There is no edge between these two nodes.")
        return 0
