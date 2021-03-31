MAX = 1000000
check = [False] * (MAX+1)
primes = []
# False가 소수, True가 소수 아님
for i in range(2, MAX+1):
    if check[i] == False:
        primes.append(i)
        temp = i
        while True:
            temp += i
            if temp > (MAX):
                break
            check[temp] = True

T = int(input())
for _ in range(T):
    N = int(input())
    # x <= y
    answer = 0
    for x in primes:
        y = N - x
        if x <= y and check[y] == False:
            answer += 1
    print(answer)