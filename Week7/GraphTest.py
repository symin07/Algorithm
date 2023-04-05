from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)


myGraph = Graph(7)

myGraph.addEdge(0, 1)
myGraph.addEdge(0, 2)
myGraph.addEdge(1, 3)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(4, 3)
myGraph.addEdge(3, 5)
myGraph.addEdge(4, 5)
myGraph.addEdge(6, 2)

print(myGraph.vertices)
print(myGraph.graph)
restult = []
insertTest = []
for currentNode in range(myGraph.vertices):
    print(myGraph.graph[currentNode])
    restult.insert(0,currentNode)
    insertTest.insert(currentNode)


