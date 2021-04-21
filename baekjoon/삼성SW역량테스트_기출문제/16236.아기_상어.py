from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 북 남 서 동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for row in range(N):
    for col in range(N):
        if board[row][col] == 9:
            s_r, s_c = row, col
            board[row][col] = 0

def bfs(row, col):
    q, visited = deque([(row, col)]), set([(row, col)])
    time = 0
    shark = 2
    eat = 0
    eat_flag = False
    answer = 0
    while q:
        size = len(q)
        # 같은 거리라면 위쪽, 왼쪽순이므로 정렬을 row, col순으로 오름차순으로
        q = deque(sorted(q, key=lambda x: (x[0], x[1])))
        for _ in range(size):
            # 가장 앞에 있는 q원소 꺼냄
            row, col = q.popleft()
            # 현재 위치에 상어보다 작은 물고기가 있어서 먹는 경우
            if 0 < board[row][col] < shark:
                board[row][col] = 0
                eat += 1
                # 상어 크기만큼 먹었으면 크기 +1
                if eat == shark:
                    shark += 1
                    eat = 0
                # 먹고 난 뒤, 현재 위치를 기준으로 다시 근처 탐색해야함
                # q와 visited 초기화
                q, visited = deque(), set([(row, col)])
                eat_flag = True
                # 먹었을때 시간 저장
                answer = time
            for i in range(4):
                nr, nc = row + dr[i], col + dc[i]
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    if board[nr][nc] <= shark:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            # 먹었으면 그 단계에서 더 돌필요 없음 (for _ in range(size))
            if eat_flag:
                eat_flag = False
                break

        time += 1
    return answer

print(bfs(s_r, s_c))