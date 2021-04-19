# 뒤에서부터 DP로 풀기
N = int(input())
reservations = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N
for i in range(N-1, -1, -1):
    day = reservations[i][0]
    pay = reservations[i][1]
    # 남은 기간보다 상담일정이 길면
    if day > N - i:
        # 마지막 날이 아니면 (dp에서는 첫번째가 아니면) 전 단계 그대로 가져옴
        if i < N-1:
            # 뒤에서부터 dp라서 이전단계 가져오는거임
            dp[i] = dp[i+1]
        continue
    # 마지막 날이고 남은 기간이 상담일정이 보다 작거나 같으면(즉 1일짜리면)
    if i == N-1:
        dp[i] = pay
    # 현재 일을 시작하면 정확히 마지막날에 끝나는 경우
    elif i + day == N:
        dp[i] = max(pay, dp[i+1])
    # 현재 일을 맡을경우와 안맡을 경우 중 큰거 고르기
    else:
        dp[i] = max(pay + dp[i + day], dp[i+1])
print(dp[0])
