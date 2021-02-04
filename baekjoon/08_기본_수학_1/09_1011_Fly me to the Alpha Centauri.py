T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x

    top = int(d ** (1/2))
    if d == top ** 2:
        print(2*top -1)
    elif d <= top ** 2 + top:
        print(2*top)
    else:
        print(2*top + 1)

    # 가장 높은 지점을 찾고 case 나눠서 생각해보기