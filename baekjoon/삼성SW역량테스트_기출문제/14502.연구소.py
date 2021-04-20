N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 4방향 탐색
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 안전영역 지역의 갯수 (0의 갯수) 를 저장할 곳
max_value = 0
# 처음 바이러스 위치(이게 bfs의 q역할을 함)
virus = []
for row in range(N):
    for col in range(M):
        if board[row][col] == 2:
            virus.append([row, col])
# 벽 3개 선정(조합)
def select_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                board[row][col] = 1
                select_wall(cnt+1)
                board[row][col] = 0

# 벽 3개 정했을때 bfs로 탐색
def bfs():
    global max_value
    # board 복사하기
    copy = [[0]*M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            copy[row][col] = board[row][col]
    value = 0
    virus2 = virus.copy()
    while virus2:
        r, c = virus2.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if copy[nr][nc] == 0:
                    copy[nr][nc] = 2
                    virus2.append([nr, nc])
    for row in range(N):
        for col in range(M):
            if copy[row][col] == 0:
                value += 1
    max_value = max(value, max_value)
select_wall(0)
print(max_value)