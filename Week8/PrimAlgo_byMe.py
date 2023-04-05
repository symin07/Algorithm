from collections import defaultdict

class Graph:
    #constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, fromEdge, toEdge, weight):
        if weight == 1:
            self.graph[fromEdge].append(toEdge)
        else: 
            self.graph[fromEdge].append(self.vertices)
            self.graph[self.vertices].append(toEdge)
            self.vertices += 1


def prims(G):
    source = G[1]
    dist = ['infinity'] * len(G.vertices)
    prev = ['empty'] * len(G.vertices)
    
    #initialize source
    prev[0] = 0
        
# G = [[0, 9, 75, 0, 0],
#      [9, 0, 95, 19, 42],
#      [75, 95, 0, 51, 66],
#      [0, 19, 51, 0, 31],
#      [0, 42, 66, 31, 0]]
myGraph = Graph(5)
myGraph.addEdge(0, 1, 1)
myGraph.addEdge(1, 2, 2)
myGraph.addEdge(1, 3, 1)
myGraph.addEdge(2, 3, 1)
myGraph.addEdge(0, 2, 2)
myGraph.addEdge(0, 5, 1)

prims(myGraph)
