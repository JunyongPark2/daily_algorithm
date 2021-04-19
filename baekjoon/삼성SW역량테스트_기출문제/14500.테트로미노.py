N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def type11(row, col):
    if col > M-4:
        return 0
    else:
        return board[row][col] + board[row][col+1] + board[row][col+2] + board[row][col+3]
def type12(row, col):
    if row > N-4:
        return 0
    else:
        return board[row][col] + board[row+1][col] + board[row+2][col] + board[row+3][col]
def type2(row, col):
    if row > N-2 or col > M-2:
        return 0
    else:
        return board[row][col] + board[row][col+1] + board[row+1][col] + board[row+1][col+1]
def type31(row, col):
    if row > N-3 or col > M-2:
        return 0
    else:
        temp1 = board[row][col] + board[row+1][col] + board[row+2][col] + max(board[row][col+1],
                                                                              board[row+1][col+1],
                                                                              board[row+2][col+1])
        temp2 = board[row][col+1] + board[row+1][col+1] + board[row+2][col+1] + max(board[row][col],
                                                                                    board[row+1][col],
                                                                                    board[row+2][col])
        return max(temp1, temp2)
def type32(row, col):
    if row > N-2 or col > M-3:
        return 0
    else:
        temp1 = board[row][col] + board[row][col + 1] + board[row][col + 2] + max(board[row + 1][col],
                                                                                  board[row + 1][col + 1],
                                                                                  board[row + 1][col + 2])
        temp2 = board[row + 1][col] + board[row + 1][col + 1] + board[row + 1][col + 2] + max(board[row][col],
                                                                                              board[row][col + 1],
                                                                                              board[row][col + 2])
        return max(temp1, temp2)
def type41(row, col):
    if row > N-3 or col > M-2:
        return 0
    else:
        temp1 = board[row][col] + board[row+1][col] + board[row+1][col+1] + board[row+2][col+1]
        temp2 = board[row+1][col] + board[row+2][col] + board[row+1][col+1] + board[row][col+1]
        return max(temp1, temp2)
def type42(row, col):
    if row > N-2 or col > M-3:
        return 0
    else:
        temp1 = board[row][col] + board[row][col+1] + board[row+1][col+1] + board[row+1][col+2]
        temp2 = board[row+1][col] + board[row+1][col+1] + board[row][col+1] + board[row][col+2]
        return max(temp1, temp2)
answer = 0
for row in range(N):
    for col in range(M):
        temp = max(type11(row, col), type12(row, col), type2(row, col), type31(row, col), type32(row, col), type41(row, col), type42(row, col))
        if temp > answer:
            answer = temp
print(answer)