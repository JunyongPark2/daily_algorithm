def move(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

def trans(direction):
    if direction == 1:
        return 0, 1
    elif direction == 2:
        return 0, -1
    elif direction == 3:
        return -1, 0
    elif direction == 4:
        return 1, 0

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))
# dice[1]이 바닥 dice[6]이 천장
dice = [0] * 7
for i in orders:
    dx, dy = trans(i)
    if 0 <= x + dx < N and 0 <= y + dy < M:
        x += dx
        y += dy
        move(i)
        if board[x][y] != 0:
            dice[1] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[1]
        print(dice[6])