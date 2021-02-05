# 에라토스테네스의 체로 풀기
M, N = map(int, input().split())
N += 1
temp = [True] * N

for i in range(2, int(N ** 0.5) + 1):
    if temp[i] == True:
        for j in range(2*i, N, i):
            temp[j] = False
temp2 = [x for x in range(2, N) if temp[x] == True]
for num in temp2:
    if num >= M:
        print(num)