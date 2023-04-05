import heapq
def Prims(G):
    
    visited = [False] * len(G)
    distance = [float('inf')] * len(G)
    prev = [None] * len(G)

    output = []

    #start vertex
    distance[0] = 0
    pq = [(0, 0)]

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue

        visited[u] = True

        if prev[u] is not None:
            output.append((prev[u], u, G[u][prev[u]]))        
        
        for v in range(len(G)):
            if G[u][v] != 0 and not visited[v] and G[u][v] < distance[v]:
                distance[v] = G[u][v]
                prev[v] = u
                heapq.heappush(pq, (distance[v], v))

    return output


input = [
        [0, 8, 5, 0, 0, 0, 0], 
        [8, 0, 10, 2, 18, 0, 0], 
        [5, 10, 0, 3, 0, 16, 0], 
        [0, 2, 3, 0, 12, 30, 14], 
        [0, 18, 0, 12, 0, 0, 4], 
        [0, 0, 16, 30, 0, 0, 26], 
        [0, 0, 0, 14, 4, 26, 0]
        ]

print(Prims(input))