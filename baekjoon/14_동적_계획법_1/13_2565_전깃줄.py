N = int(input())
connect_list = [list(map(int, input().split())) for _ in range(N)]
connect_list.sort(key=lambda x: x[0])
dp = [1] * N

for i in range(N):
    for j in range(i):
        if connect_list[i][1] > connect_list[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N - max(dp))