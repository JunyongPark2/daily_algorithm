N = int(input())
person_list = []
answer_list = []
for _ in range(N):
    person_list.append(list(map(int, input().split())))

for i in range(N):
    cnt = 0
    for j in range(N):
        if person_list[i][0] < person_list[j][0] and person_list[i][1] < person_list[j][1]:
            cnt += 1
    answer_list.append(str(cnt+1))
print(' '.join(answer_list))