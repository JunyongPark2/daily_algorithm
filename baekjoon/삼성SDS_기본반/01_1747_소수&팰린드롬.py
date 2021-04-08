# 소수 목록 구하기
MAX = 1000001
sieve = [False]*2 + [True]*(MAX-2)
for i in range(2, int(MAX**0.5)+1):
    if sieve[i] == True:
        for j in range(i+i, MAX, i):
            sieve[j] = False
# 팰린드롬 구하기
def my_func(x):
    if x == int(str(x)[::-1]):
        return True
    return False

N = int(input())
answer = 0
for i in range(N, MAX):
    if i == 1:
        continue
    if sieve[i] and my_func(i):
        answer = i
        break
# N보다 큰 소수&팰린드롬이 없는경우 
if answer == 0:
    answer = 1003001
print(answer)