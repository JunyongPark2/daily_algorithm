N = int(input())
my_list = []
for _ in range(N):
    my_list.append(int(input()))
# 버블 정렬
for i in range(len(my_list)-1):
    for j in range(len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

for i in my_list:
    print(i)