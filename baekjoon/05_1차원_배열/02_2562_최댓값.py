my_list = []
for i in range(9):
    my_list.append(int(input()))

max_value = 0
max_index = 0
for i, num in enumerate(my_list):
    if num > max_value:
        max_value = num
        max_index = i
print(max_value)
print(max_index+1)