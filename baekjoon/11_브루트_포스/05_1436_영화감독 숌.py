N = int(input())
i = 1
cnt = 0
while True:
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break
    i += 1