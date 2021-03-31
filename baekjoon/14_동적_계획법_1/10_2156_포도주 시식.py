n = int(input())

wines = [int(input()) for _ in range(n)]

dp = [0] * n
if n == 1:
    print(wines[0])
elif n == 2:
    print(wines[0] + wines[1])
else:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])
    # case 1 : i번째 포도주를 먹고 i-1번째 포도주도 먹은 경우 => i-2번째는 먹으면 안됨
    # case 2 : i번째 포도주를 먹고 i-1번째 포도주는 안먹은 경우
    # case 3 : i번째 포도주를 안먹은 경우
    for i in range(3, n):
        case1 = dp[i-3] + wines[i-1] + wines[i]
        case2 = dp[i-2] + wines[i]
        case3 = dp[i-1]
        dp[i] = max(case1, case2, case3)
    print(dp[n-1])