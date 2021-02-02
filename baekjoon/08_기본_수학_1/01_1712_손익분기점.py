A, B, C = map(int, input().split())
if C <= B:
    print(-1)
else:
    term = A/(C-B)
    print(int(term)+1)