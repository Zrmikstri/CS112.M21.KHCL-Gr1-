def print_board(board):
    for i in range(len(board)):
        print(*board[i])
        print()

def isValid(board, row, col):
    # Check row
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    # Check backslash diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check slash diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col):
    if col == len(board):
        return True
    for row in range(len(board)):
        if isValid(board, row, col):
            board[row][col] = 1
            if solve(board, col+1):
                return True
            board[row][col] = 0
    return False

if __name__ == "__main__":
    n = int(input())
    matrix = [[0]*n for _ in range(n)]
    if solve(matrix, 0):
        print_board(matrix)
    else:
        print(-1)