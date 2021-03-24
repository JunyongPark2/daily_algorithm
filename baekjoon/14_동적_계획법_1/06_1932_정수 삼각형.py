n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
for row in range(1, len(triangle)):
    for col in range(len(triangle[row])):
        if col == 0:
            triangle[row][col] += triangle[row-1][col]
        elif col == len(triangle[row])-1:
            triangle[row][col] += triangle[row-1][col-1]
        else:
            triangle[row][col] += max(triangle[row-1][col], triangle[row-1][col-1])
print(max(triangle[-1]))