N = int(input())
people = []
for i in range(N):
    people.append(input().split()+[i])
sorted_people = sorted(people, key=lambda x : (int(x[0]),x[2]))
for person in sorted_people:
    print(' '.join(person[:2]))