N = int(input())
for _ in range(N):
    my_str = input()
    my_list = my_str.split('X')
    score = 0
    for i in my_list:
        score += len(i)*(len(i)+1)/2
    print(int(score))