
# SUDOKU GAME


# display board after solving
def displayBoard(board):

    for i in range(0,len(board)):
        print(board[i])



# check if the value is correct for the position or not
# check horizontally , vertically , sub matrix of 3 X 3
def isValid(board, row, col, val):

    for x in range(0,len(board)):
        if board[row][x] == val:
            return False

    for x in range(0,len(board)):
        if board[x][col] == val:
            return False

    smr = (row//3) * 3
    smc = (col//3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if board[smr+i][smc+j] == val:
                return False


    return True


# recursive sudoku solver

def solveSudoku(board, row, col):

    # gives the first answer
    if row == len(board):  # if the row reaches extreme
       return True


    nr = 0
    nc = 0
    if col == len(board)-1:
        nc = 0
        nr = row + 1
    else:
        nr = row
        nc = col + 1

    if board[row][col] != -1:
        if solveSudoku(board, nr, nc):
            return True

    for i in range(1, len(board) + 1):
        if isValid(board, row, col, i):
            board[row][col] = i
            if solveSudoku(board, nr, nc):
                return True
            board[row][col] = -1

    return False



def sudoku(board):

    solvable = solveSudoku(board, 0, 0)  # lets start from left uppermost box
    if solvable:
        displayBoard(board)
    else:
        print("Non Solvable Sudoku")


if __name__ == '__main__':
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]


    sudoku(example_board)
