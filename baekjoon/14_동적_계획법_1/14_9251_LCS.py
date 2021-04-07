# 2차원 dp
str1 = input()
str2 = input()
n1 = len(str1)
n2 = len(str2)

# 초기값 0
dp = [[0]*(n2+1) for _ in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      
print(dp[n1][n2])