N = int(input())
memo = [1, 1, 2] + [0] * (N-2)

for i in range(3, N+1):
    memo[i] = (memo[i-2] + memo[i-1]) % 15746
print(memo[N])