N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

first = 0
second = 0
# 총감독관 처리
for i in range(len(A)):
    A[i] -= B
    first += 1
# 부감독관 처리
for i in range(len(A)):
    if A[i] <= 0:
        continue
    elif A[i] <= C:
        second += 1
    else:
        if A[i] % C == 0:
            second += A[i] // C
        else:
            second += A[i] // C + 1
print(first + second)