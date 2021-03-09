def combination(n,r):
    if r > n-r:
        r = n-r
    answer = 1
    for _ in range(r):
        answer *= n
        n -= 1
    for _ in range(r):
        answer //= r
        r -= 1
    return answer

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combination(M,N))