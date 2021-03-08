N, K = map(int, input().split())
if K > N-K:
    K = N-K
answer = 1
for _ in range(K):
    answer *= N
    N -= 1

for _ in range(K):
    answer /= K
    K -= 1

print(int(answer))