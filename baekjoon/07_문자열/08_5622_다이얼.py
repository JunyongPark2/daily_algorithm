T = input()
answer = 0
for i in T:
    if i in 'ABC':
        answer += 3
    elif i in 'DEF':
        answer += 4
    elif i in 'GHI':
        answer += 5
    elif i in 'JKL':
        answer += 6
    elif i in 'MNO':
        answer += 7
    elif i in 'PQRS':
        answer += 8
    elif i in 'TUV':
        answer += 9
    elif i in 'WXYZ':
        answer += 10

print(answer)