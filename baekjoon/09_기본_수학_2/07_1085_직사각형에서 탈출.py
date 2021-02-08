x, y, w, h = map(int, input().split())

dist_x = min(abs(x), abs(x-w))
dist_y = min(abs(y), abs(y-h))
print(min(dist_x, dist_y))