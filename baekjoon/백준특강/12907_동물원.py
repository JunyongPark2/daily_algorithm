N = int(input())
answers = list(map(int, input().split()))
# 모두 같은 동물일 때보다 큰 수가 나오면 조합의 수 0
if max(answers) > N-1:
    print(0)
else:    
    my_list = [0] * N
    for answer in answers:
        my_list[answer] += 1
        # 같은 수가 3개 이상 나오면 조합의 수 0
        if my_list[answer] > 2:
            print(0)
            break
    # for문을 다 돌리면
    else:
        # 2의 개수 세기
        cnt_2 = 0
        # 내림차순이 아니면 조합의 수 0
        for i in range(N-1):
            if my_list[i] < my_list[i+1]:
                print(0)
                break
            if my_list[i] == 2:
                cnt_2 += 1
        # 무사히 for문을 다 돌면
        else:
            # 토끼와 고양이의 수가 같으면
            if N % 2 == 0 and cnt_2 == N//2:
                print(2**cnt_2)
            # 그렇지 않으면
            else:
                print(2**(cnt_2+1))