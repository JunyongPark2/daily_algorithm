# 내장 모듈 collections의 Counter 사용
# list의 각각 갯수를 반환
# .most_commons() 사용하면 가장 빈도가 많은 수를 튜플로 묶어 리스트로 반환



import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))


if N == 1:
    # 산술평균
    print(arr[0])
    # 중앙값
    print(arr[0])
    # 최빈값
    print(arr[0])
    # 범위
    print(0)
else:
    arr.sort()
    # 산술평균
    mean = round(sum(arr)/N)
    print(mean)
    # 중앙값
    median = arr[N//2]
    print(median)
    # 최빈값
    modes = Counter(arr).most_common()
    if modes[0][1] == modes[1][1]:
        print(modes[1][0])
    else:
        print(modes[0][0])
    # 범위
    print(arr[-1] - arr[0])





















# 시간초과
# # 버블정렬
# for i in range(len(my_list), -1, -1):
#     for j in range(i-1):
#         if my_list[j] > my_list[j+1]:
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# # 산술평균
# num_sum = 0
# for num in my_list:
#     num_sum += num
# mean = round(num_sum / N)
# print(mean)

# # 중앙값
# median = my_list[N//2]
# print(median)

# # 최빈값
# my_dict = {}
# for num in my_list:
#     my_dict[num] = my_dict.get(num, 0) + 1
# new_dict = sorted(my_dict.items(), key=lambda x : x[1])
# if new_dict[0][1] == new_dict[1][1]:
#     print(new_dict[1][0])

# # 범위
# print(my_list[-1]-my_list[0])