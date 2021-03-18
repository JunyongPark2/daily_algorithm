memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def w(a, b, c):
    global memo
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    # memoization에 값이 있으면 그대로 출력
    elif memo[a][b][c]:
        return memo[a][b][c]
    # 값이 없는 경우
    elif a < b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]
    else:
        memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[a][b][c]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    answer = w(a,b,c)

    print(f'w({a}, {b}, {c}) = {answer}')