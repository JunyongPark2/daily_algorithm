from copy import deepcopy

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def food(array, row, col):
    positions = []
    direction = array[row][col][1]
    for i in range(1, 4):
        nr, nc = row + i*dr[direction], col + i*dc[direction]
        if 0 <= nr < 4 and 0 <= nc < 4 and 1 <= array[nr][nc][0] <= 16:
            positions.append([nr, nc])
    return positions

def fish_position(array, idx):
    for row in range(4):
        for col in range(4):
            if array[row][col] == idx:
                return (row, col)
    return None

def fish_move(array, shark_r, shark_c):
    # 1번 물고기부터 16번 물고기까지
    for idx in range(1, 17):
        position = fish_position(array, idx)
        if position is None:
            continue
        row, col = position[0], position[1]
        direction = array[row][col][1]
        for j in range(8):
            nr, nc = row + dr[direction], col + dc[direction]
            if 0 <= nr < 4 and 0 <= nc < 4 and not (nr == shark_r and nc == shark_c):
                array[row][col][0], array[nr][nc][0] = array[nr][nc][0], array[row][col][0]
                array[row][col][1], array[nr][nc][1] = array[nr][nc][1], direction
                break
            direction = (direction + 1) % 8

def backtracking(array, row, col, total):
    global answer
    array = deepcopy(array)

    # 해당 위치 물고기 먹기
    number = array[row][col][0]
    array[row][col][0] = -1

    # 물고기 이동
    fish_move(array, row, col)

    # 상어가 이동할 수 있는 후보 확인
    result = food(array, row, col)

    # 해당 먹이 먹는 모든 과정 탐색

    answer = max(answer, total + number)
    for next_r, next_c in result:
        backtracking(array, next_r, next_c, total + number)


# 4 by 4 공간 정의 [번호, 방향]
board = [[[0, 0] for _ in range(4)] for _ in range(4)]
for row in range(4):
    temp = list(map(int, input().split()))
    for col in range(4):
        board[row][col] = [temp[2*col], temp[2*col+1]-1]
answer = 0
backtracking(board, 0, 0, 0)
print(answer)

