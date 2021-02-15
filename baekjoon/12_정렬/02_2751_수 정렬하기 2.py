N = int(input())
my_list = []
for _ in range(N):
    my_list.append(int(input()))
# 내장 함수
my_list.sort()
for i in my_list:
    print(i)