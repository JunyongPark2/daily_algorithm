N, M = map(int, input().split())
card_list = list(map(int, input().split()))
answer = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = card_list[i] + card_list[j] + card_list[k]
            if answer < temp <= M:
                answer = temp
               
print(answer)