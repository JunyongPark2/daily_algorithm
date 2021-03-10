# 뒤에 0의 갯수는 결국 5의 몇승인지에 따라 결정됨.
# 2는 항상 5의 갯수보다 많음.
N = int(input())
cnt = 0
for i in range(N+1):
    temp = i
    while temp >= 5:
        if temp % 5 == 0:
            cnt += 1
            temp //= 5
        else:
            break
print(cnt)