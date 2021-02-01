T = input()
my_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in my_list:
    while i in T:
        T = T.replace(i, '0')
print(len(T))