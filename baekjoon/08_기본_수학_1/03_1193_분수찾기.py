X = int(input())
if X == 1:
    print('1/1')
else:
    cnt = 1
    i = 1
    while True:
        if X > i:
            X -= i
            cnt += 1
            i += 1
        else:
            remainder = X
            break
    if cnt % 2 == 0:
        up = remainder
        down = cnt + 1 - remainder
    else:
        up = cnt + 1 - remainder
        down = remainder
    print(f'{up}/{down}')