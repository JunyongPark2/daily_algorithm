N = int(input())
A= list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
# 정렬 후 이분 탐색으로 풀기
A.sort()

def binary_search(arr, key):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return 0

for m in B:
    print(binary_search(A, m))