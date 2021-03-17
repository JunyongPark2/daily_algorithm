T = int(input())
for _ in range(T):
    N = int(input())
    dp = [(1, 0), (0, 1)] + [(0, 0)] * (N-1)
    for i in range(2, N+1):
        dp[i] = (dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1])
    print(*dp[N])