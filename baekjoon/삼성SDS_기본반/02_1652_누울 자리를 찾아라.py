N = int(input())
board = [list(input()) for _ in range(N)]
horizontal = 0
vertical = 0

cnt_row = 0
cnt_col = 0
# 가로 검사
for row in range(N):
    for col in range(N):
        if board[row][col] == '.':
            cnt_row += 1
        else:
            if cnt_row >= 2:
                horizontal += 1
            cnt_row = 0
    # 마지막이 .으로 끝나는 경우 확인해줘야함
    if cnt_row >= 2:
        horizontal += 1
    cnt_row = 0

# 세로 검사
for col in range(N):
    for row in range(N):
        if board[row][col] == '.':
            cnt_col += 1
        else:
            if cnt_col >= 2:
                vertical += 1
            cnt_col = 0
    # 마지막이 .으로 끝나는 경우 확인해줘야함
    if cnt_col >= 2:
        vertical += 1
    cnt_col = 0

print(horizontal, vertical)