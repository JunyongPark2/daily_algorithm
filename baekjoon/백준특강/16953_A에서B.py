A, B = map(int, input().split())
cnt = 1

while True:
    if B % 2 == 0:
        B //= 2
        cnt += 1
    elif B % 10 == 1:
        B //= 10
        cnt += 1
    else:
        cnt = -1
        break
    if B == A:
        break
    elif B < A:
        cnt = -1
        break
print(cnt)