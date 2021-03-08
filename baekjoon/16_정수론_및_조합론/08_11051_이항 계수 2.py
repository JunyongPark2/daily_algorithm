# 뤼카의 정리?

N, K = map(int, input().split())
if N >= 10007:
    print(0)
else:
    if K > N-K:
        K = N-K
    answer = 1
    for _ in range(K):
        answer *= N
        N -= 1

    for _ in range(K):
        answer //= K
        K -= 1

    print(int(answer) % 10007)