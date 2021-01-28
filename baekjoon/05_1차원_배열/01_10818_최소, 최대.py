N = int(input())
my_list = list(map(int, input().split()))

min_num = my_list[0]
max_num = my_list[0]

for num in my_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(min_num, max_num)