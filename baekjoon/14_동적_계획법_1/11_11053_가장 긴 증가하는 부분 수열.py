N = int(input())
A = list(map(int, input().split()))
# dp[i]에 A[i]보다 작은 수를 count(단 0 ~ i-1까지), dp[0] 는 자동으로 1
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
