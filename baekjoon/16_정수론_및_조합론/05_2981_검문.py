N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list.sort()
def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a
diff = [num_list[i+1]-num_list[i] for i in range(N-1)]

if len(diff) == 1:
    divisor = diff[0]
else:
    divisor = diff[0]
    for i in range(1, len(diff)):
        divisor = GCD(divisor, diff[i])
answer = [divisor]
for i in range(2, int(divisor**0.5)+1):
    if divisor % i == 0:
        answer.append(i)
        # divisor의 제곱근까지 구하고 나머지는 몫으로 하면 효율적임
        if divisor // i != i:
            answer.append(divisor//i)
answer.sort()
print(' '.join(map(str, answer)))