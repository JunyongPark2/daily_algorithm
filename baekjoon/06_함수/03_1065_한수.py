N = int(input())

def hansu(k):
    if k < 100:
        return True
    else:
        temp = [int(x) for x in str(k)]
        for i in range(len(temp)-2):
            if temp[i] - temp[i+1] != temp[i+1] - temp[i+2]:
                return False
        else:
            return True

cnt = 0
for num in range(1, N+1):
    if hansu(num):
        cnt += 1
print(cnt)
         