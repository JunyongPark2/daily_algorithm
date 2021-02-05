N = int(input())

while True:
    if N == 1:
        break
    for i in range(2, round(N//2+1)):
        if N % i == 0:
            print(i)
            N = N // i
            break
    else:
        print(N)
        break