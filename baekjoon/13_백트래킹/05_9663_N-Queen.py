N = int(input())
cnt = 0
# 세로축과 대각선 축의 가능한 인덱스를 생각
# 예를 들어 N=5인 경우 대각선 원소들의 row, col idx합이 8까지 가능
vertical, diag1, diag2 = [False]*N, [False]*(2*N-1), [False]*(2*N-1)

def dfs(row):
    global cnt
    # 가장 아래 인덱스는 N-1이므로 row가 무사히 N까지 왔으면 cnt+1하고 반환
    if row == N:
        cnt += 1
        return
    # column을 돌면서
    for col in range(N):
        # 각 idx가 모두 False일때 들어갈 수 있음
        if not (vertical[col] or diag1[row+col] or diag2[row-col+N-1]):
            vertical[col] = diag1[row+col] = diag2[row-col+N-1] = True
            dfs(row+1)
            vertical[col] = diag1[row+col] = diag2[row-col+N-1] = False

dfs(0)
print(cnt)