import heapq

def greedyMove(puzzle, currentIndex, visited):    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    candiForMove = []
    for i in range(4):
        newRow = int(str(currentIndex[0])) + dx[i]
        newColumn = int(str(currentIndex[1])) + dy[i]
        candiMov = newRow, newColumn
        if newRow >= 0 and newColumn >= 0 and newRow < len(puzzle) and newColumn < len(puzzle[0]):
            if candiMov not in visited:
                candiForMove.append([newRow, newColumn, puzzle[newRow][newColumn]])

    greedMove = list(candiForMove[0])
    maxValue = abs(candiForMove[0][2] - puzzle[currentIndex[0]][currentIndex[1]])
    for i in range(1, len(candiForMove)):
        if (abs(candiForMove[i][2] - puzzle[currentIndex[0]][currentIndex[1]]) 
            < abs(candiForMove[i-1][2] - puzzle[currentIndex[0]][currentIndex[1]])):
            greedMove = list(candiForMove[i])
            maxValue = abs(candiForMove[i][2] - puzzle[currentIndex[0]][currentIndex[1]])
        else:  
            greedMove = list(candiForMove[i-1])
            maxValue = abs(candiForMove[i-1][2] - puzzle[currentIndex[0]][currentIndex[1]])
    
    rtnGreedy = greedMove[0], greedMove[1]
    return rtnGreedy, maxValue
    # return maxValue


def minEffort(puzzle):
    startIndex = puzzle[0][0]
    currentIndex = 0, 0
    destination = len(puzzle) - 1, len(puzzle[0]) - 1
    visited = []
    result = [] 
    while currentIndex != destination:
        visited.append(currentIndex)
        tempRt = greedyMove(puzzle, currentIndex, visited)  
        currentIndex = tempRt[0]
        maxValue = tempRt[1]
        result.append(currentIndex)

    return maxValue
puzzle = [[1,3,5], [2,8,3], [3,4,5], [8,9,4]]
print(minEffort(puzzle))