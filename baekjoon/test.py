def trans(number):
    if number == 0:
        return 3, 1
    row = (number-1) // 3
    col = (number-1) % 3
    return [row, col]


for i in range(10):
    print(i)
    print(trans(i))