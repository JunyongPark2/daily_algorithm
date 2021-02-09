n = int(input())

def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibo(x-1) + fibo(x-2)
    
print(fibo(n))