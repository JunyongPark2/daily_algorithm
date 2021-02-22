import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(trees)
while left <= right:
    mid = (left + right)//2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total < M:
        right = mid - 1
    else:
        left = mid + 1
print(right)
