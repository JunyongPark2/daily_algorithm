N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
# 끝나는 시간을 기준으로 정렬, 만약 끝나는 시간이 같으면 시작하는 시간을 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))
cur_time = 0
cnt = 0
for start, end in meetings:
    # 미팅의 시작시간이 현재 시간 이후면 현재시간을 해당 미팅의 종료시간으로 바꾸고 count 
    if start >= cur_time:
        cur_time = end
        cnt += 1
print(cnt)