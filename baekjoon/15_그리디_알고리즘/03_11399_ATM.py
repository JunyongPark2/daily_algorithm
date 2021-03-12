N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
temp = 0
answer = 0
for time in time_list:
    temp += time
    answer += temp
print(answer)