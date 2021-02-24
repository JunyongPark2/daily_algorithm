# 최장 증가 부분 수열
N = int(input())
A = list(map(int, input().split()))

def binary(my_list, key):
    left, right = 0, len(my_list)-1
    while left < right:
        mid = (left + right)//2
        if my_list[mid] < key:
            left = mid + 1
        elif my_list[mid] > key:
            right = mid
        else:
            left = right = mid
    return right

D = [0]
for num in A:
    if D[-1] < num:
        D.append(num)
    else:
        D[binary(D, num)] = num
print(len(D)-1)