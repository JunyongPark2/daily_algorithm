# Knapsack Algorithm
# 2차원 DP

# N : 물건 갯수, K : 최대 무게
N, K = map(int, input().split())

items = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
# 굳이 한칸 더 만드는 이유는 index로 바로 무게를 맞추기 위해
dp = [[0]*(K+1) for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(1, K+1):
        weight = items[n][0]
        value = items[n][1]

        if k < weight:
            dp[n][k] = dp[n-1][k]
        else:
            dp[n][k] = max(value + dp[n-1][k-weight], dp[n-1][k])
print(dp[N][K])