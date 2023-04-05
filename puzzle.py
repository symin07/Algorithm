
puzzleTable = {0:1, 1:2}
def puzzleTopdwon(n):
    if n in puzzleTable:
        return puzzleTable[n]
    puzzleTable[n] = puzzleTopdwon(n-1) + puzzleTopdwon(n-2)
    return puzzleTable[n]

def puzzleBottomup(n):
    if n in puzzleTable:
        return puzzleTable[n]
        for i in range(2, n):
            puzzleTable[i] = puzzleTable[i-1] + puzzleTable[i-2]
    return puzzleTable[n]

def bruteForce(n):   
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return puzzleTopdwon(n-1) + puzzleTopdwon(n-2)
    


print("4 puzzles", puzzleTopdwon(4))
print("5 puzzles", puzzleTopdwon(5))
print("5 puzzles", puzzleTopdwon(6))

print("4 puzzles", puzzleBottomup(4))
print("5 puzzles", puzzleBottomup(5))
print("5 puzzles", puzzleBottomup(6))


print("4 puzzles", bruteForce(4))
print("5 puzzles", bruteForce(5))
print("5 puzzles", bruteForce(6))