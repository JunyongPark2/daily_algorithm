A, B, V = map(int, input().split())
answer = (V-B)/(A-B)
if answer == int(answer):
    print(int(answer))
else:
    print(int(answer)+1)

# 처음에 리스트로 만드니 메모리 초과,
# while문 만들어 부등식으로 만드니 시간 초과,
# 좀 더 간단한 방법을 찾지 못함. 간단하게 생각하자.