# Case 잘 나눠서 생각하기
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    # 두 원이 일치하는 경우
    if dist == 0 and r1 == r2:
        print(-1)
    # 외접, 내접
    elif dist == r1+r2 or dist == abs(r2-r1):
        print(1)
    # 만나지 않는 경우 완전 멀거나 한 원이 다른원 포함
    elif max(dist, r1, r2) > dist + r1 + r2 - max(dist, r1, r2):
        print(0)
    # 나머지 두 점에서 만나는 경우
    else:
        print(2)