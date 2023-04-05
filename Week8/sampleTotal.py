from collections import defaultdict
import heapq as pq

class NegativeEdgeException(Exception):
    pass

class Graph(object):
    """Graph data structure, undirected and no weight by default"""

    def __init__(self, conncetions, directed=False, Weighted=False):
        # If weighted, connection should be a dict of tuple pairs:
        # int_edgeWeight, otherwise, a list of tuples
        self._graph = defaultdict(set)
        self._wight = defaultdict(int)
        self._directed = directed
        self._weighted = Weighted
        if not self.weighted:
            self.add_connection(connections)
        else:
            self._negativeEdges = False
            self.add_weighted(connections)

    def add_connectios(self, connections):
        # Add connections (list of tuple pairs) to graph
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        # Add connections between node1 and node2
        self._graph