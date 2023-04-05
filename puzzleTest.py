

def puzzleTopdwon(n, puzzleList):
    puzzleList = 0 *[n]
    if n == 1:
        puzzleList[0] = 1
    elif n == 2:
        puzzleList[1] = 2
    if n in puzzleList:
        return puzzleList[n]
    else:
        puzzleList[n] = puzzleTopdwon(n-1, puzzleList) + puzzleTopdwon(n-2, puzzleList)
    return puzzleList[n]

def puzzleBottomup(n, result):
    puzzleTable = [0]*n
    puzzleTable[0] = 1
    puzzleTable[1] = 2 

    if n == 1:
        result = puzzleTable[0]
    elif n == 2:
        result = puzzleTable[1]        
    else:
        for i in range(2, n):
            puzzleTable[i] = puzzleTable[i-1] + puzzleTable[i-2]
            result = puzzleTable[i]       
    return result

def bruteForce(n, result):   
    bfArray = [n][n]


puzzleList = []
print("4 puzzles", puzzleTopdwon(4, puzzleList))
print("5 puzzles", puzzleTopdwon(5, puzzleList))
print("5 puzzles", puzzleTopdwon(6, puzzleList))

print("4 puzzles", puzzleBottomup(4, result))
print("5 puzzles", puzzleBottomup(5, result))
print("5 puzzles", puzzleBottomup(6, result))