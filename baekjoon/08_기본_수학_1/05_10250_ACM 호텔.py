T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    Y = N % H
    X = (N // H) + 1
    if Y == 0:
        Y = H
        X -= 1
    print(100*Y+X)

# N이 H로 나누어 떨어진 경우 Y는 0이 된다.
# 따라서 0층 대신 H층으로 대입해야하고 X 또한 넘어간걸 다시 1 빼줘야함.