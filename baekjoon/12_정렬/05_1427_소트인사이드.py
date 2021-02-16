num_list = list(map(int, list(input())))
num_list.sort(reverse=True)
answer = list(map(str, num_list))
print(''.join(answer))