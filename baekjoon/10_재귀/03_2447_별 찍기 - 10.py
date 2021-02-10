def star(n):
    global output

    if n == 3:
        output[0][:3] = ['*', '*', '*']
        output[1][:3] = ['*', ' ', '*']
        output[2][:3] = ['*', '*', '*']
    else:
        nn = n // 3
        star(nn)
        for row in range(3):
            for col in range(3):
                if row == 1 and col == 1:
                    continue
                for k in range(nn):
                    output[nn*row + k][nn*col:nn*(col+1)] = output[k][:nn]
N = int(input())

output = [[' ' for _ in range(N)] for _ in range(N)]
star(N)
for line in output:
    print(''.join(line))