# 공유기 최대 거리를 타겟으로 이분탐색!
N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]
# 이분 탐색은 정렬 후 사용
x.sort()
# 공유기 최소 거리 1
left = 1
right = x[-1] - x[0]

while left <= right:
    mid = (left + right)//2
    current = x[0]
    cnt = 1

    for i in range(1, N):
        # 현재 위치와 다음 위치의 거리가 공유기 간 최소거리보다 크면 됨.
        if x[i] >= current + mid:
            cnt += 1
            current = x[i]

    # 공유기 간 최소거리가 mid일 때, 공유기 간 거리가 mid보다 큰 경우가 C 보다 크면
    # 공유기 간 최소거리를 늘리자.
    if cnt >= C:
        left = mid + 1
    # 공유기 간 최소거리가 mid일 때, 공유기 간 거리가 mid보다 큰 경우가 C 보다 작으면
    # 공유기 간 최소거리를 줄이자.
    else:
        right = mid - 1
print(right)