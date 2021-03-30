N, K, M = map(int, input().split())

cnt = 0
while True:
    cnt += 1
    if K % (N-cnt+1) == 0:
        temp = N - cnt + 1
    else:
        temp = K % (N-cnt+1)

    if M == temp:
        break

    if M > temp:
        M = M - temp
    else:
        M = M - temp + N - cnt + 1

print(cnt)