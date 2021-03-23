N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    costs[i][0] = costs[i][0] + min(costs[i-1][1], costs[i-1][2])
    costs[i][1] = costs[i][1] + min(costs[i-1][0], costs[i-1][2])
    costs[i][2] = costs[i][2] + min(costs[i-1][0], costs[i-1][1])
print(min(costs[-1]))