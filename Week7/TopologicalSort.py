from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

def helperFunction(myGraph, currentNode, visited, result):
    visited[currentNode] = True                             # Mart the currnet node as visited

    # Recur for all the adjacent vertices of currentNode
    for i in myGraph.graph[currentNode]:
        if visited[i] == False:
            helperFunction(myGraph, i, visited, result)
    
    result.insert(0,currentNode)

def topologicalSort(myGraph):
    visited = [False] * myGraph.vertices    # Mark all the vertices as not visited
    result = []                             # Our stack to store the result/output

    for currentNode in range(myGraph.vertices):
        if visited[currentNode] == False:
            helperFunction(myGraph, currentNode, visited, result)

    return result



myGraph = Graph(7)
myGraph.addEdge(0, 1)
myGraph.addEdge(0, 2)
myGraph.addEdge(1, 3)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 5)
myGraph.addEdge(4, 3)
myGraph.addEdge(4, 5)
myGraph.addEdge(6, 2)

for Node in range(myGraph.vertices):
    print("[",Node, "]:", myGraph.graph[Node])

print("Topological Sort")
result = topologicalSort(myGraph)
for Node in range(myGraph.vertices):
    print("[",result[Node], "]:", myGraph.graph[result[Node]])

