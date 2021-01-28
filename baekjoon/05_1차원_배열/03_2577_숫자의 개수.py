A = int(input())
B = int(input())
C = int(input())

D = str(A * B * C)
my_dict = dict()
for i in range(10):
    my_dict[str(i)] = D.count(str(i))
    
for value in my_dict.values():
    print(value)