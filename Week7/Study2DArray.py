puzzle = [[1,3,5], [2,8,3], [3,4,5], [1,2,6]]
start = 0, 0
current = start
print(current)
destination = len(puzzle) - 1, len(puzzle[0]) - 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]

while current != destination:
    print("here")
    current = destination
for i in range(4):
    rowCheck = current[0] + dx[i]
    columnCheck = current[1] + dy[i]
    if rowCheck >= 0 and columnCheck >= 0 and rowCheck < len(puzzle) and columnCheck < len(puzzle[0]):
        print("updwon, leftright", puzzle[rowCheck][columnCheck])

print(current)
pathString = 'D' 
direction = 'D'

tempString = pathString + direction
print(tempString)
pathString = 'EE' 
direction = 'EE'
tempString = pathString + direction
print(tempString)
