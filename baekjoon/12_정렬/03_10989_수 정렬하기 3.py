# 메모리를 줄이기 위해 input()대신 sys.stdin.readlin()로 사용
# Python3로 하니까 통과되는데 Pypy3로하면 통과안됨. 왜그런지모르겠음.

import sys
N = int(input())

count_list = [0] * 10001
for i in range(N):
    count_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if count_list[i]:
        for j in range(count_list[i]):
            print(i)


# 카운팅 정렬 메모리 초과됨 단순히 출력만 하면 될듯
# k = max(my_list)
# count_list = [0] * (k+1)
# answer_list = [0] * N

# for i in range(N):
#     count_list[my_list[i]] += 1
# for i in range(k):
#     count_list[i+1] += count_list[i]
# for i in range(N-1, -1, -1):
#     answer_list[count_list[my_list[i]]-1] = my_list[i]
#     count_list[my_list[i]] -= 1
# for i in answer_list:
#     print(i)