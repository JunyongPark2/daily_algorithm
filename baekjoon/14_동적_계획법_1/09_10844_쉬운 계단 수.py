N = int(input())
dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for i in range(1, N+1):
    temp = [0] * 10
    temp[0] = dp[i-1][1]
    for j in range(1, 9):
        temp[j] = dp[i-1][j-1] + dp[i-1][j+1]
    temp[9] = dp[i-1][8]
    dp.append(temp)
print(sum(dp[N-1])%1000000000)