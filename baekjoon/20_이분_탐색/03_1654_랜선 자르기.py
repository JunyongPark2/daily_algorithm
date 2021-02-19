K, N = map(int, input().split())
my_list = [int(input()) for _ in range(K)]
left, right = 1, max(my_list)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in my_list:
        cnt += i // mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1
print(right)