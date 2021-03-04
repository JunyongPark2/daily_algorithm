T = int(input())
for _ in range(T):
        
    A, B = map(int, input().split())
    big = max(A, B)
    small = min(A, B)
    # 유클리드 호제법
    def GCD(a, b):
        while b != 0:
            a, b = b, a%b
        return a

    def LCM(a, b):
        return a*b // GCD(a,b)
    print(LCM(big, small))