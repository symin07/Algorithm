def solve_puzzle(puzzle, source, destination):
    # Check if source and destination cells are valid
    if source[0] < 0 or source[0] >= len(puzzle) or source[1] < 0 or source[1] >= len(puzzle[0]):
        return None
    if destination[0] < 0 or destination[0] >= len(puzzle) or destination[1] < 0 or destination[1] >= len(puzzle[0]):
        return None
    
    # Initialize the queue for Breadth-First Search
    queue = [(source, [source])]
    
    # Keep track of visited cells to avoid loops
    visited = set()
    visited.add(source)
    
    # Breadth-First Search
    while queue:
        (current_row, current_col), path = queue.pop(0)
        if (current_row, current_col) == destination:
            return path
        for row_offset, col_offset, direction in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            next_row, next_col = current_row + row_offset, current_col + col_offset
            if (next_row, next_col) in visited or next_row < 0 or next_row >= len(puzzle) or next_col < 0 or next_col >= len(puzzle[0]) or puzzle[next_row][next_col] == '#':
                continue
            visited.add((next_row, next_col))
            queue.append(((next_row, next_col), path + [(next_row, next_col)]))
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
