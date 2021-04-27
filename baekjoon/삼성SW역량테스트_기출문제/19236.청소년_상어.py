import copy

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


# 상어가 먹을 수 있는 후보들 위치 반환
def food(array, shark_r, shark_c):
    positions = []
    shark_d = array[shark_r][shark_c][1]
    for i in range(1, 4):
        nr, nc = shark_r + dr[shark_d], shark_c + dc[shark_d]
        if 0 <= nr < 4 and 0 <= nc < 4 and 1 <= array[nr][nc][0] <= 16:
            positions.append([nr, nc])
        shark_r, shark_c = nr, nc
    return positions


def fish_position(array, idx):
    for row in range(4):
        for col in range(4):
            if array[row][col][0] == idx:
                return (row, col)
    return None


def fish_move(array, shark_r, shark_c):
    # 1번 물고기부터 16번 물고기까지
    for i in range(1, 17):
        position = fish_position(array, i)
        if position is None:
            continue
        fish_r, fish_c = position[0], position[1]
        fish_d = array[fish_r][fish_c][1]
        for j in range(8):
            nr, nc = fish_r + dr[fish_d], fish_c + dc[fish_d]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if not (nr == shark_r and nc == shark_c):
                    array[fish_r][fish_c][0], array[nr][nc][0] = array[nr][nc][0], array[fish_r][fish_c][0]
                    array[fish_r][fish_c][1], array[nr][nc][1] = array[nr][nc][1], fish_d
                    break
            fish_d = (fish_d + 1) % 8


def backtracking(array, shark_r, shark_c, total):
    global answer
    array = copy.deepcopy(array)

    # 해당 위치 물고기 먹기 (먹은 자리는 번호를 -1로 바꿔줌)
    number = array[shark_r][shark_c][0]
    array[shark_r][shark_c][0] = -1

    # 물고기 이동
    fish_move(array, shark_r, shark_c)

    # 상어가 이동할 수 있는 후보 확인
    result = food(array, shark_r, shark_c)

    # 해당 먹이 먹는 모든 과정 탐색
    answer = max(answer, total + number)
    for next_r, next_c in result:
        backtracking(array, next_r, next_c, total + number)



# 4 by 4 공간 정의 [번호, 방향]
array = [[[0, 0] for _ in range(4)] for _ in range(4)]
for row in range(4):
    temp = list(map(int, input().split()))
    for col in range(4):
        array[row][col] = [temp[2 * col], temp[2 * col + 1] - 1]
answer = 0
backtracking(array, 0, 0, 0)
print(answer)
