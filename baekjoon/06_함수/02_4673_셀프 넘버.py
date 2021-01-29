def d(n):
    answer = n
    for i in str(n):
        answer += int(i)
    
    return answer

yes = {d(x) for x in range(1, 10000) if d(x) < 10000}

for i in range(1, 10000):
    if i not in yes:
        print(i)