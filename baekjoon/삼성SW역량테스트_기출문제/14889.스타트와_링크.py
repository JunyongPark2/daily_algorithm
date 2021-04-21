N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
def dfs(idx, cnt):
    global answer
    # 종료 조건
    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if i != j:
                    if visited[i] and visited[j]:
                        start += board[i][j]
                    elif not visited[i] and not visited[j]:
                        link += board[i][j]
        answer = min(answer, abs(start-link))
    # 방문
    for i in range(idx, N):
        if visited[i] == False:
            visited[i] = True
            dfs(i+1, cnt+1)
            visited[i] = False
answer = 100 * 10 * 9
dfs(0, 0)
print(answer)