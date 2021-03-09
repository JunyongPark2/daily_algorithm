T = int(input())
for _ in range(T):
    n = int(input())
    my_list = [input().split()[1] for _ in range(n)]
    my_dict = {}
    for i in my_list:
        my_dict[i] = my_dict.get(i, 0) + 1
    answer_list = list(my_dict.values())
    
    answer = 1
    for i in answer_list:
        answer *= i+1
    print(answer-1)