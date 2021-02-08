while True:
    num_list = list(map(int, input().split()))
    if sum(num_list) == 0:
        break
    square_list = sorted([x**2 for x in num_list])
    if square_list[2] == square_list[0] + square_list[1]:
        print('right')
    else:
        print('wrong')

