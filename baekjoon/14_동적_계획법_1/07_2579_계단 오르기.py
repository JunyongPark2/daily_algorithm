N = int(input())
scores = [int(input()) for _ in range(N)]
# 리스트는 주소를 참조하므로 copy로 복사해야함
answer = scores.copy()
if N == 1:
    print(scores[0])
elif N == 2:
    print(scores[0] + scores[1])
elif N == 3:
    print(max(scores[0] + scores[2], scores[1] + scores[2]))
else:
    # answer[i]는 i가 도착점일때 가질수 있는 가장 높은 점수
    answer[0] = scores[0]
    answer[1] = scores[0] + scores[1]
    answer[2] = max(scores[0] + scores[2], scores[1] + scores[2])
    # i를 기준으로 i-1을 밟았는지 아닌지로 나눔
    for i in range(3, N):
    # max 첫번째 요소에 answer[i-1] + scores[i]하지 않은 이유는 i-2와 i-1모두 밟았으면 i번째는 불가능하기 때문
        answer[i] = max(answer[i-3] + scores[i-1] + scores[i], answer[i-2] + scores[i])
    print(answer[-1])