import heapq
def createGraph(puzzle):
    startOfGraph = puzzle[0][0]
 
    # make edge between neighbor nodes
    dx = [0,0,-1,1]         # up and down             
    dy = [-1,1,0,0]         # left and right

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            for k in range(4):
                puzzleGraph = {str(i) + str(j) }  



def minEffort(puzzle):
   # puzzleGraph = createGraph(puzzle)
   # distances = {element: float('infinity') for element in puzzle}
    start = 0, 0 
    pq = [(0, start)]
    distances = []
    visited = []

    while len(pq) > 0:
        current_distance, current_addr = heapq.heappop(pq)
        distances.append(current_distance)
        visited.append(current_addr)

        if current_addr == (len(puzzle) - 1, len(puzzle[0]) - 1):
            break

        dx = [0,0,-1,1]         # UP AND DOWN 
        dy = [-1,1,0,0]         # LEFR AND RIGHT

        for i in range(4):
            newRow = current_addr[0] + dx[i]
            newColumn = current_addr[1] + dy[i]
            if newRow >= 0 and newColumn >= 0 and newRow < len(puzzle) and newColumn < len(puzzle[0]):
                if (newRow, newColumn) not in visited:
                    current_distance = abs(puzzle[newRow][newColumn] - puzzle[current_addr[0]][current_addr[1]])
                    heapq.heappush(pq, (current_distance, (newRow, newColumn)))
            
    return max(distances)

    # Nodes can get added to the priority queue multiple times, We
    # only process a vertex the first time we remove it from the priority queue

        



puzzle = [[1,3,5,1,2,3], [2,8,3,1,2,3], [3,4,5,6,7,3], [8,9,4,3,8,3]]
print(minEffort(puzzle))