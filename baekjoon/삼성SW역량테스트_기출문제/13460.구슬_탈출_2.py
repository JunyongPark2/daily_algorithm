# BFS로 풀기
N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
queue = []
# 4차원 방문배열 [Red_r][Red_c][Blue_r][Blue_c]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# 초기설정, 빨간공과 파란공의 위치를 찾고 queue에 넣고 방문처리함.
def pos_init():
    rr, rc, br, bc = 0, 0, 0, 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 'R':
                rr, rc = row, col
            elif board[row][col] == 'B':
                br, bc = row, col
    # 마지막 1은 10번 횟수제한있어서 횟수 체크에 미리 넣어놓음
    queue.append((rr, rc, br, bc, 1))
    visited[rr][rc][br][bc] = True

# 현재위치에서 방향을 넣고 이동하는 함수
def move(r, c, dr, dc):
    # 이동 칸 수
    cnt = 0
    # 다음이 벽이거나 현재가 구멍일때까지 반복
    while board[r+dr][c+dc] != '#' and board[r][c] != '0':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

def solve():
    pos_init()
    while queue:
        rr, rc, br, bc, depth = queue.pop(0)
        if depth > 10:
            break
        # 4방향 탐색
        for i in range(4):
            # 빨간 공
            nrr, nrc, rcnt = move(rr, rc, dr[i], dc[i])
            # 파란 공
            nbr, nbc, bcnt = move(br, bc, dr[i], dc[i])
            # 새로 구한 파란공의 좌표가 구멍이 아니면 (즉 실패조건이 아니면)
            if board[nbr][nbc] != '0':
                # 빨간공의 좌표가 구멍이면 (즉 성공조건)
                if board[nrr][nrc] == '0':
                    print(depth)
                    return
                # 좌표가 겹치면
                if nrr == nbr and nrc == nbc:
                    # 더 많이 이동한 공을 한칸 다시 back
                    if rcnt > bcnt:
                        nrr -= dr[i]
                        nrc -= dc[i]
                    else:
                        nbr -= dr[i]
                        nbc -= dc[i]
                # 방문한적 없으면
                if not visited[nrr][nrc][nbr][nbc]:
                    # 방문처리 후
                    visited[nrr][nrc][nbr][nbc] = True
                    # queue에 넣음
                    queue.append((nrr, nrc, nbr, nbc, depth+1))
    # 실패해서 break된 경우
    print(-1)
solve()