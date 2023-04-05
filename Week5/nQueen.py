def isAttack(row, col, board, N):
    # vertical
    for i in range(N):
        if board[row][i] == 1:
            return True
    # Horizontal 
    for i in range(N):
        if board[i][col] == 1:
            return True
    ## diagonal
    # FROM LEFT TOP TO RIGHT BOTTOM
    if row >= col:
        for i in range(0, N-(row-col)):
            if board[row-col+i][col-col+i] == 1:
                return True
    else:
        for i in range(0, N-(col-row)):
            if board[row-row+i][col-row+i] == 1:
                return True

    # FROM LEFT BOTTOM TO RIGHT TOP
    if row + col >= N - 1:          
        for i in range(0, N-(row+col+1-N)):
            if board[N-1-i][row+col+1-N+i] == 1:
                return True
    else:
        for i in range(0, row+col+1):
            if board[0+i][row+col-i] == 1:
                return True
    
    return False

def solve_nQueens(board, row, N, remaining):
    #base case
    if (remaining == 0):
        return True
    for col in range(N):
        if(isAttack(row, col, board, N)):
            pass
        else: 
            board[row][col] = 1
            if(solve_nQueens(board, row+1, N, remaining-1)):
                return True
        #backTrack if any placement results in no solution
        board[row][col] = 0
    return False



def nQueens(N):
    board = [[0 for x in range(N)] for x in range(N)]
    solve_nQueens(board, 0, N, N)
    return board


board = nQueens(4)
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()


    solve_n_Queens(board, row, N, remaining):
    #base case
    if(remaining == 0) : return True
    for col := 1 to N
        if(is_attacked(row, col, board, N)):
            # skip the cell and continue
        else:
            # Place the queen and recursively solve for remaining queens
            board[row][col] = 1
            if(solve_n_Queens(board, row+1,N, remaining-1)):
                return True
            #backtrack if any placement results in no solution
            board[row][col]=0
    return False

def combination_sum_helper(nums, start, result, remainder, combination):
  #Base case
  if(remainder == 0):
      result.append(combination)
      return
  elif( remainder <0):
      return # sum exceeded the target
 
  for i := start to len(nums)-1:
      combination.append(nums[i])
      combination_sum_helper(nums, i, result, remainder-nums[i], combination)
      #backtrack
      combination.pop()
 
 
def combination_sum(nums, target):
  result = []
  combination_sum_helper(nums,0, result, target,[])

