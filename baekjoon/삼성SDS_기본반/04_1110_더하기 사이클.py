N = input()
answer = N
cnt = 0
while True:
    if int(N) < 10:
        N = '0' + N
    temp = int(N[0]) + int(N[1])
    N = str(int(N[1] + str(temp)[-1]))
    cnt += 1
    # print(f"temp {cnt}: {temp}, N: {N}")
    if N == answer:
        break
print(cnt)