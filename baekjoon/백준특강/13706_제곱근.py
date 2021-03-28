N = int(input())
# 이분탐색?
left = 1
right = N // 2
while left <= right:
    mid = (left + right) // 2
    if mid ** 2 == N:
        print(mid)
        break
    elif mid ** 2 > N:
        right = mid - 1
    else:
        left = mid + 1
