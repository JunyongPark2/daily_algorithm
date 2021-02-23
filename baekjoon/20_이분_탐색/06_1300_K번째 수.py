N = int(input())
k = int(input())

left = 1
# k 번째 수는 k보다 클 수가 없다.
right = k

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    # A 행렬은 index 1부터 시작하므로 1~N
    for i in range(1, N+1):
        # i행에 x보다 작은 숫자의 갯수는 x를 i로 나눈 몫임 (단, N보다 클 수 없음)
        cnt += min(mid//i, N)

    if cnt < k:
        left = mid + 1
    else:
        right = mid - 1
print(left)
