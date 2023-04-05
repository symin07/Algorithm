def solve_puzzle(puzzle, source, destination):
    
    # Initialize the queue for Breadth-First Search
    pathString = str()
    tempString = str()
    queue = [(source, [source], pathString)]
    
    # Keep track of visited cells to avoid loops
    visited = set()
    visited.add(source)
    
    # Breadth-First Search
    while queue:
        (current_row, current_col), path, pathString = queue.pop(0)
        if (current_row, current_col) == destination:
            return path, pathString
        for row_offset, col_offset, direction in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            next_row, next_col = current_row + row_offset, current_col + col_offset
            if (next_row, next_col) in visited or next_row < 0 or next_row >= len(puzzle) or next_col < 0 or next_col >= len(puzzle[0]) or puzzle[next_row][next_col] == '#':
                continue
            visited.add((next_row, next_col))
            tempString = pathString + direction
            queue.append(((next_row, next_col), path + [(next_row, next_col)], tempString))
    # If there is no valid path, return None
    return None


Puzzle = [
            ['-', '-', '-', '-', '-'],
            ['-', '-', '#', '-', '-'],
            ['-', '-', '-', '-', '-'], 
            ['#', '-', '#', '#', '-'], 
            ['-', '#', '-', '-', '-']
        ]

print(solve_puzzle(Puzzle, (0,4), (4,4)))
print(solve_puzzle(Puzzle, (0,0), (0,4)))
print(solve_puzzle(Puzzle, (0,2), (2,2)))
print(solve_puzzle(Puzzle, (0,0), (4,4)))

