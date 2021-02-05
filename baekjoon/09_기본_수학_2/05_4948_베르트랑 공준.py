# 변수 명 안헷갈리게 조심...
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for num in range(n+1, 2*n+1):
        if num == 2:
            cnt += 1
            continue
        for k in range(2, int(num**0.5)+1):
            if num % k == 0:
                break
        else:
            cnt += 1
    print(cnt)