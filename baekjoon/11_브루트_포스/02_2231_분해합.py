def generator(n):
    temp = n
    for i in str(n):
        temp += int(i)
    return temp

N = int(input())
for i in range(N+1):
    if generator(i) == N:
        print(i)
        break
else:
    print(0)