# 재귀에서 원하는 결과를 바로 얻었을때 정상적으로 종료하는 함수 sys.exit(0)
# 비정상적으로라도 종료하고 싶으면 sys.exit(1)
import sys

board = [list(map(int, input().split())) for _ in range(9)]
# 0의 위치 파악
zero_list = [[row, col] for row in range(9) for col in range(9) if board[row][col] == 0]

def dfs(idx):
    # 다 채우면 출력
    if idx == len(zero_list):
        for row in board:
            print(*row)
        sys.exit(0)
    x = zero_list[idx][0]
    y = zero_list[idx][1]
    # 작은 박스 검사를 위한 작업
    xx = (x//3) * 3
    yy = (y//3) * 3

    # 숫자를 사용했는지 체크 리스트
    check_list = [0] + [1 for _ in range(9)]
    for i in range(9):
        # 가로 검사
        if board[x][i]:
            check_list[board[x][i]] = 0
        # 세로 검사
        if board[i][y]:
            check_list[board[i][y]] = 0
    # 작은 박스 검사
    for row in range(xx, xx+3):
        for col in range(yy, yy+3):
            if board[row][col]:
                check_list[board[row][col]] = 0
    # check_list에 1인 숫자만 가져오기
    candidate_list = []
    for i in range(len(check_list)):
        if check_list[i] == 1:
            candidate_list.append(i)

    # 백트래킹 하나씩 넣어보기
    for num in candidate_list:
        board[x][y] = num
        dfs(idx+1)
        board[x][y] = 0
dfs(0)