# Helper Code
from collections import defaultdict
import heapq


class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units
        self.distances = {}

    def add_node(self, value):
        """
        add a node to the graph.
        :param value: node to be added
        :type value: str
        """
        self.nodes.add(value)
        if value not in self.distances:
            self.distances[value] = {}

    def add_edge(self, from_node, to_node, distance):
        """
        add edge between two nodes in the graph.
        """
        self.distances[from_node][to_node] = distance
        self.distances[to_node][from_node] = distance    # lets make the graph undirected / bidirectional

    def print_graph(self):
        """ print the graph as a dictionary """
        print("Set of Nodes are: ", self.nodes)
        print("Distances are: ", self.distances)


def dijkstra(graph, source):
    """
    Dijkstra's algorithm to find the shortest distance between source node and all other nodes in the graph.

    :param graph: Graph object with vertices and edges( nodes and distances between them)
    :type graph: Graph
    :param source: Source node from which the distance to all other nodes is to be found
    :type source: str
    :return: Dictionary with key as node and value as distance from source node
    :rtype: dict
    """
    result = dict.fromkeys(graph.nodes, float('inf'))
    path = {}
    result[source] = 0
    priority_queue = [(0, source)]
    visited = set()
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)  # Get unvisited node with the minimum distance
        visited.add(curr_node)
        # 1. Find the unvisited node having smallest known distance from the source node.

        for neighbour, distance in graph.distances[curr_node].items():
            if neighbour not in visited:
                relaxed_val = result[curr_node] + graph.distances[curr_node][neighbour]
                if relaxed_val < result[neighbour]:
                    result[neighbour] = relaxed_val
                    path[neighbour] = curr_node
                    heapq.heappush(priority_queue, (relaxed_val, neighbour))

    return result

def test_dijkstra_shortest_path():
    # Test 1
    test_graph = Graph()
    for node in ['A', 'B', 'C', 'D', 'E']:
        test_graph.add_node(node)
    test_graph.add_edge('A','B',3)
    test_graph.add_edge('A','D',2)
    test_graph.add_edge('B','D',4)
    test_graph.add_edge('B','E',6)
    test_graph.add_edge('B','C',1)
    test_graph.add_edge('C','E',2)
    test_graph.add_edge('E','D',1)
    #print(test_graph.print_graph())
    print(dijkstra(test_graph, 'A'))     # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}


def main():
    test_dijkstra_shortest_path()
if __name__ == '__main__':
    main()