
import sys
def solve_tsp(G):
    
    visited = []
    
    # initialize node as startNode = 0, and visit 0
    node = 0 
    visited.append(0)
   
    # from the startNode to endNode
    while len(visited) < len(G):
        
        # get minNode which is the nextNode to visit
        nextNode = G[node].index(min(G[node]))
        
        # not visited or connected
        if nextNode not in visited and G[node][nextNode] != 0:
            visited.append(nextNode)
            node = nextNode
        
        # visited node or not connected
        else:
            G[node][nextNode] = sys.maxsize 

    visited.append(0)
    
    return visited


 

G = [[0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0]]
    
print(solve_tsp(G))
# test incomplete Grraph 
IG = [[0, 2, 3, 0, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [0, 2, 20, 0, 9],
    [1, 20, 13, 9, 0]]

print(solve_tsp(IG))
