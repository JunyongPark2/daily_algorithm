def move_a_to_c(k, a, b, c):
    if k == 1:
        move_list.append([a, c])
    else:
        move_a_to_c(k-1, a, c, b)
        move_a_to_c(1, a, b, c)
        move_a_to_c(k-1, b, a, c)

N = int(input())
move_list = []
move_a_to_c(N, '1', '2', '3')
print(len(move_list))
for move in move_list:
    print(' '.join(move))