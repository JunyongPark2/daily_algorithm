N, K = map(int, input().split())
A = list(map(int, input().split()))

# # 완전탐색(당연히 시간초과날듯)
# cnt = 0
# for p in range(N-2):
#     for q in range(p+1, N-1):
#         for r in range(q+1, N):
#             if A[p] * A[q] * A[r] % K == 0:
#                 cnt += 1
# print(cnt)


# K를 소인수 분해하자
K_clone = K
K_dict = {}
i = 2
while K_clone != 1:
    if K_clone % i == 0:
        K_clone //= i
        K_dict[i] = K_dict.get(i, 0) + 1
    else:
        i += 1

# A의 원소들은 K의 소인수들의 갯수를 세자.
A_list = []
for a in A:
    a_dict = {}
    i = 2
    while a != 1:
        if a % i == 0:
            a //= i
            a_dict[i] = a_dict.get(i, 0) + 1
        else:
            i += 1
    A_list.append(a_dict)