# 2차원배열 copy를 위해서 내장모듈 써야함
from copy import deepcopy

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def move(idx):
    # 위로 기울였을때
    if idx == 0:
        for col in range(N):
            idx = 0
            # 순서주의
            for row in range(1, N):
                # 값이 존재하면
                if board[row][col]:
                    temp = board[row][col]
                    board[row][col] = 0
                    if board[idx][col] == 0:
                        board[idx][col] = temp
                    elif board[idx][col] == temp:
                        board[idx][col] = temp*2
                        idx += 1
                    else:
                        idx += 1
                        board[idx][col] = temp
    # 아래로 기울였을때
    elif idx == 1:
        for col in range(N):
            idx = N-1
            # 순서주의!
            for row in range(N-2, -1, -1):
                if board[row][col]:
                    temp = board[row][col]
                    board[row][col] = 0
                    if board[idx][col] == 0:
                        board[idx][col] = temp
                    elif board[idx][col] == temp:
                        board[idx][col] = temp*2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][col] = temp 
    # 왼쪽으로 기울였을때
    elif idx == 2:
        for row in range(N):
            idx = 0
            # 순서주의!
            for col in range(1, N):
                if board[row][col]:
                    temp = board[row][col]
                    board[row][col] = 0
                    if board[row][idx] == 0:
                        board[row][idx] = temp
                    elif board[row][idx] == temp:
                        board[row][idx] = temp*2
                        idx += 1
                    else:
                        idx += 1
                        board[row][idx] = temp 
    # 오른쪽으로 기울였을때
    else:
        for row in range(N):
            idx = N-1
            # 순서주의!
            for col in range(N-2, -1, -1):
                if board[row][col]:
                    temp = board[row][col]
                    board[row][col] = 0
                    if board[row][idx] == 0:
                        board[row][idx] = temp
                    elif board[row][idx] == temp:
                        board[row][idx] = temp*2
                        idx -= 1
                    else:
                        idx -= 1
                        board[row][idx] = temp

def step(cnt):
    global answer, board
    if cnt == 5:
        for row in range(N):
            answer = max(answer, max(board[row]))
        return
    
    temp = deepcopy(board)
    for idx in range(4):
        move(idx)
        step(cnt+1)
        board = deepcopy(temp)

step(0)
print(answer)