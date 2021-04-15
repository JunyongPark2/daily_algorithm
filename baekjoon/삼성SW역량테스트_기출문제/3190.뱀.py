from collections import deque

# idx : 상(0) 우(1) 하(2) 좌(3)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def change_vec(vec, s):
    # 왼쪽회전 : 상(0) -> 좌(3) -> 하(2) -> 우(1)
    if s == 'L':
        vec = (vec-1) % 4
    # 오른쪽회전 : 상(0) -> 우(1) -> 하(2) -> 좌(3)
    else:
        vec = (vec+1) % 4
    return vec

def start():
    vec = 1
    time = 1
    head_r, head_c = 0, 0
    visited = deque([[head_r, head_c]])
    # 2가 뱀의 몸이 있는곳
    board[head_r][head_c] = 2
    while True:
        head_r, head_c = head_r + dr[vec], head_c + dc[vec]
        # 종료조건(벽에 부딪히거나, 자신의 몸과 부딪히면)이 아니면 
        if 0 <= head_r < N and 0 <= head_c < N and board[head_r][head_c] != 2:
            # 사과가 없으면
            if board[head_r][head_c] != 1:
                # 가장 왼쪽걸 꺼내고
                tail_r, tail_c = visited.popleft()
                # 보드에 0처리
                board[tail_r][tail_c] = 0
            board[head_r][head_c] = 2
            visited.append([head_r, head_c])
            if time in times.keys():
                vec = change_vec(vec, times[time])
            time += 1
        # 종료 조건
        else:
            return time                
N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    apple_r, apple_c = map(int, input().split())
    # 문제에서 1행1열로 시작해서 편의상 -1로함
    board[apple_r-1][apple_c-1] = 1
L = int(input())
# 딕셔너리로 time을 받아서 나중에 호출하기 쉽게
times = {}
for _ in range(L):
    X, C = input().split()
    times[int(X)] = C
print(start())