def prime_num(k):
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            return False
    else:
        return True

T = int(input())
for _ in range(T):
    n = int(input())
    left = n//2
    right = n//2

    while True:
        if prime_num(left) and prime_num(right):
            break
        else:
            left -= 1
            right += 1
    print(left, right)