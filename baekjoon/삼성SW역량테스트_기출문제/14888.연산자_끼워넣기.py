N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))
min_value = 1000000000
max_value = -1000000000

def cal(left, right, i):
    if i == 0:
        return left + right
    elif i == 1:
        return left - right
    elif i == 2:
        return left * right
    else:
        if left < 0:
            return -(-left//right)
        else:
            return left//right

def f(idx, cur):
    global min_value
    global max_value
    # 종료 조건
    if idx == N-1:
        if cur > max_value:
            max_value = cur
        if cur < min_value:
            min_value = cur
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            f(idx+1, cal(cur, A[idx+1], i))
            operators[i] += 1
f(0, A[0])
print(max_value)
print(min_value)