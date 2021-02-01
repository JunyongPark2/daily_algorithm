N = int(input())
answer = 0
for i in range(N):
    T = input()
    temp = [T[0]]
    for j in T:
        if j != temp[-1]:
            temp.append(j)
    if len(set(temp)) == len(temp):
        answer +=1
print(answer)
