first, second = map(int, input().split())
big = max(first, second)
small = min(first, second)
# 유클리드 호제법
def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def LCM(a, b):
    return a*b // GCD(a,b)
print(GCD(big, small))
print(LCM(big, small))