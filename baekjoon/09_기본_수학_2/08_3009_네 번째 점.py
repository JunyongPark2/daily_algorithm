a =list(map(int, input().split()))
b =list(map(int, input().split()))
c =list(map(int, input().split()))

x = [a[0], b[0], c[0]]
y = [a[1], b[1], c[1]]

d = []
# x축
if a[0] == b[0]:
    d.append(c[0])
elif a[0] == c[0]:
    d.append(b[0])
else:
    d.append(a[0])
# y축
if a[1] == b[1]:
    d.append(c[1])
elif a[1] == c[1]:
    d.append(b[1])
else:
    d.append(a[1])
print(d[0], d[1])