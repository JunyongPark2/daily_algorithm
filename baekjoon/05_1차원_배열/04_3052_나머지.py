my_list = []
for i in range(10):
    my_list.append(int(input()))

remainder = {x % 42 for x in my_list}
print(len(remainder))