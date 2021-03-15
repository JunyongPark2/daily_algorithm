my_input = input()
my_input2 = my_input.split('-')
my_input3 = [i.split('+') for i in my_input2]
for i in range(len(my_input3)):
    for j in range(len(my_input3[i])):
        my_input3[i][j] = int(my_input3[i][j])
for i in range(len(my_input3)):
    my_input3[i] = sum(my_input3[i])
answer = my_input3[0]
for i in range(1, len(my_input3)):
    answer -= my_input3[i]
print(answer)