N = int(input())
if N == 1:
    cnt = 1
else:
    cnt = 2
    N -= 1
    i = 6
    while True:
        if N > i:
            N -= i
            cnt += 1
            i += 6
        else:
            break
print(cnt)