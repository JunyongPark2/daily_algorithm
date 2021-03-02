N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
total = 0
for row in range(N):
    for col in range(N):
        total += board[row][col]
num_list = list(range(N))
sel = [0] * (N//2)

check = [0] * N
perm_list = []
def perm(idx):
    if idx == N//2:
        perm_list.append(sel.copy())
    else:
        for i in range(N):
            if check[i] == 0 and (idx == 0 or num_list[i] > sel[idx-1]):
                sel[idx] = num_list[i]
                check[i] = 1
                perm(idx+1)
                check[i] = 0
perm(0)
answer = 100000000
for case in perm_list:
    temp1 = 0
    temp2 = 0
    for row in range(N):
        for col in range(N):
            if (row in case) and (col in case):
                temp1 += board[row][col]
            elif (row not in case) and (col not in case):
                temp2 += board[row][col]
    if abs(temp1 - temp2) < answer:
        answer = abs(temp1 - temp2)
print(answer)