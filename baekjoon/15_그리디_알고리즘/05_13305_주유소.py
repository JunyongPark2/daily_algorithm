N = int(input())
distances = list(map(int, input().split()))
cities = list(map(int, input().split()))

min_price = 1000000000
answer = 0
for i in range(N-1):
    if cities[i] < min_price:
        min_price = cities[i]
    answer += min_price * distances[i]
print(answer)