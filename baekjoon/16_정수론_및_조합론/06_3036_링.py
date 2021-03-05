N = int(input())
rings = list(map(int, input().split()))
first = rings[0]
def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a
for i in range(1, N):
    a = first // GCD(first, rings[i])
    b = rings[i] // GCD(first, rings[i])
    print('{}/{}'.format(a, b))