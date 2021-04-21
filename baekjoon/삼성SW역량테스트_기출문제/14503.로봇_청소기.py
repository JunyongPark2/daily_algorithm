N, M = map(int, input().split())
cur_r, cur_c, d = map(int, input().split())
# 0 : 북, 1 : 동, 2 : 남, 3 : 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def left(x):
    return (x-1) % 4

board = [list(map(int, input().split())) for _ in range(N)]
# 초기 설정 (청소한 곳을 2로 표시)
board[cur_r][cur_c] = 2
cnt = 1
while True:
    dd = d
    # step b
    for i in range(4):
        # step a
        dd = left(dd)
        nr = cur_r + dr[dd]
        nc = cur_c + dc[dd]

        if board[nr][nc] == 0:
            cnt += 1
            cur_r, cur_c = nr, nc
            board[cur_r][cur_c] = 2
            d = dd
            break
    # 4방향 다 돌았는데 break 걸리지 않으면
    else:
        cur_r -= dr[d]
        cur_c -= dc[d]
        if board[cur_r][cur_c] == 1:
            break
print(cnt)
