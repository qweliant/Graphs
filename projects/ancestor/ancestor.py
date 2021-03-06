import sys
sys.path.append('../')

from graph.util import Stack, Queue

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):

    g = Graph()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(child, parent)

    s = Stack()
    s.push([starting_node])
    print("starting_node: ", starting_node)
    longest_path_length = 1
    earliest_ancestor = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]
        print("path: ", path, "current_node: ", current_node)

        if len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        neighbors = g.get_neighbors(current_node)

        for ancestor in neighbors:
            path_copy = list(path)
            print("path_copy: ", path_copy)
            path_copy.append(ancestor)
            s.push(path_copy)

    return earliest_ancestor
