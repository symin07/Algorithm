# def isAttack(row, col, board, N):
#     # vertical
#     for i in range(N):
#         if board[row][i] == 1:
#             return False
#     # Horizontal 
#     for i in range(N):
#         if board[i][col] == 1:
#             return False
#     ## diagonal
#     # ++ -- diagonal
#     if row >= col:
#         for i in range(N-(row+1)):
#             if board[row+i][col+i] == 1:
#                 return False
#         for i in reversed(range(col)):
#             if board[row-i][col-i] == 1:
#                     return False          
#     else:
#         for i in range(N-(col+1)):
#             if board[row+i][col+i] == 1:
#                     return False
#         for i in reversed(range(row)):
#             if board[row-i][col-i] == 1:
#                     return False
#     # +-, -+ diagonal    
#     if row <= N-(col+1):                 # row's remaining is less than col's remaining
#         for i in reversed(range(row+1)):
#             if board[row-i][col+i] == 1:
#                 return False
#         for i in range(row):
#             if board[row+i][col-i] == 1:
#                 return False

#     else:                               # row's remaining is greater than col's remaining
#         for i in reversed(range(N-(col+1)):
#             if board[row-i][col+i] == 1:
#                 return False
#         for i   board[row+i][col-i] == 1:
#                 return False

    
    


#     for i in range(N):
#         if board[i][col] == 1:
#             return False

# def solve_nQueens(board, row, N, remaining):
#     #base case
#     if (remaining == 0):
#         return True
#     for col in range(len(N)):
#         if(isAttack(row, col, board, N)):

#     else:
        
#         if(isAttack(row, col, board))
#     return 



# def nQueens(N):
#     board = [[0 for x in range(N)] for x in range(N)]
#     solve_nQueens(board, 0, N, N)
#     return board


# board = nQueens(4)
# print(board) 



######################## answer#
def is_attacked(row, col, board, N):
    #check row
    for i in range(N):
        if(board[row][i] == 1):
            return True

    #check column
    for i in range(N):
        if(board[i][col] == 1):
            return True

    #check upper left diagonal cells
    row_p = row-1
    col_p = col-1
    while(row_p>=0 and col_p>=0):
        if(board[row_p][col_p] == 1):
            return True
        row_p -=1
        col_p -=1
    #check upper right diagonal cells
    row_p = row-1
    col_p = col +1
    while(row_p>=0 and col_p<N):
        if(board[row_p][col_p] ==1):
            return True
        row_p -=1
        col_p +=1

    return False


def solve_n_Queens(board,row, N, remaining):
    #base case if solved for N rows return
    if(remaining==0):
        return True

    for col in range(N):
        if(is_attacked(row, col, board, N)):
            continue           #skip the attacked cell
        else:
            board[row][col] = 1
            if(solve_n_Queens(board, row+1,N, remaining-1)): # recursively solve for solution
                return True
            #backtrack if any placement results in no solution
            board[row][col]=0
    return False



def n_Queens(N):
    board = [[0 for x in range(N)] for x in range(N)]

    solve_n_Queens(board,0, N, N)
    return board


print(n_Queens(5))