T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floor = list(range(1, n+1))

    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]
    print(floor[-1])

# 처음부터 너무 효율성만 생각하지말고
# 어떤 원리인지 파악부터 하자.