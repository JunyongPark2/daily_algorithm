T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    temp = ''
    for j in S:
        temp += R * j
    print(temp)
