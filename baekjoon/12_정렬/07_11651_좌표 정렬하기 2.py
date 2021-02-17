N = int(input())
dots = []
for _ in range(N):
    dots.append(list(map(int, input().split())))
answer = sorted(dots, key=lambda x : (x[1], x[0]))
for dot in answer:
    print(' '.join(map(str, dot)))