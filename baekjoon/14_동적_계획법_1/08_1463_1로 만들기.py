N = int(input())
answer = [0, 0, 1, 1]
for i in range(4, N+1):
    # -1의 경우
    answer.append(answer[i-1] + 1)
    # /2의 경우
    if i % 2 == 0:
        answer[i] = min(answer[i], answer[i//2] + 1)
    # /3의 경우
    if i % 3 == 0:
        answer[i] = min(answer[i], answer[i//3] + 1)
print(answer[N])