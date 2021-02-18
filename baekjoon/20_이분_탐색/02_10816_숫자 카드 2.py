from sys import stdin
# 이분 탐색으로 풀기

_ = stdin.readline()
num_list = sorted(list(map(int, stdin.readline().split())))
_ = stdin.readline()
M_list = map(int, stdin.readline().split())
def binary_search(arr, key, left, right):
    if left > right:
        return 0
    mid = (left + right)//2
    if key == arr[mid]:
        return arr[left:right+1].count(key)
    elif key < arr[mid]:
        return binary_search(arr, key, left, mid-1)
    else:
        return binary_search(arr, key, mid+1, right)

answer = {}
for n in num_list:
    left = 0
    right = len(num_list) - 1
    if n not in answer:
        answer[n] = binary_search(num_list, n, left, right)

print(' '.join(str(answer[x]) if x in answer else '0' for x in M_list))