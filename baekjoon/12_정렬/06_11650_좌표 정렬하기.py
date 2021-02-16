N = int(input())

dots = []
for _ in range(N):
    dots.append(list(map(int, input().split())))

answer = sorted(dots, key=lambda x : (x[0], x[1]))
for dot in answer:
    print(' '.join(list(map(str, dot))))