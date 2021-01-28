C = int(input())

for _ in range(C):
    temp_list = list(map(int, input().split()))
    N = temp_list[0]
    scores = temp_list[1:]
    over_avg = sum([1 for score in scores if score > sum(scores)/N])
    answer = round(100 * over_avg/N,3)
    print(f"{answer:.3f}%")