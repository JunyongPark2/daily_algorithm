cards = []
for _ in range(5):
    card = input().split()
    cards.append([card[0], int(card[1])])

def rule1(my_arr):
    for i in range(1, 5):
        if my_arr[i][0] != my_arr[i-1][0]:
            return False
    else:
        temp = []
        for i in range(5):
            temp.append(my_arr[i][1])
        temp.sort()
        for i in range(1, 5):
            if temp[i] - temp[i-1] != 1:
                return False
        else:
            return 900 + temp[-1]

def rule2(my_arr):
    temp = []
    for i in range(5):
        temp.append(my_arr[i][1])
    temp.sort()
    if temp[0] == temp[1] == temp[2] == temp[3]:
        return 800 + temp[0]
    elif temp[1] == temp[2] == temp[3] == temp[4]:
        return 800 + temp[1]
    else:
        return False

def rule3(my_arr):
    temp = []
    for i in range(5):
        temp.append(my_arr[i][1])
    temp.sort()
    if temp[0] == temp[1] == temp[2] and temp[3] == temp[4]:
        return 700 + temp[0]*10 + temp[3]
    elif temp[0] == temp[1] and temp[2] == temp[3] == temp[4]:
        return 700 + temp[0] + temp[2]*10
    else:
        return False

def rule4(my_arr):
    for i in range(1, 5):
        if my_arr[i][0] != my_arr[i-1][0]:
            return False
    else:
        temp = []
        for i in range(5):
            temp.append(my_arr[i][1])
        return 600 + max(temp)

def rule5(my_arr):
    temp = []
    for i in range(5):
        temp.append(my_arr[i][1])
    temp.sort()
    for i in range(1, 5):
        if temp[i] - temp[i-1] != 1:
            return False
    else:
        return 500 + temp[-1]

def rule6(my_arr):
    temp = []
    for i in range(5):
        temp.append(my_arr[i][1])
    temp.sort()
    if temp[0] == temp[1] == temp[2]:
        return 400 + temp[0]
    elif temp[1] == temp[2] == temp[3]:
        return 400 + temp[1]
    elif temp[2] == temp[3] == temp[4]:
        return 400 + temp[2]
    else:
        return False

def rule7(my_arr):
    temp = []
    for i in range(5):
        temp.append(my_arr[i][1])
    temp.sort()
    if temp[0] == temp[1] and temp[2] == temp[3]:
        return 300 + temp[2]*10 + temp[0]
    elif temp[0] == temp[1] and temp[3] == temp[4]:
        return 300 + temp[3]*10 + temp[0]
    elif temp[1] == temp[2] and temp[3] == temp[4]:
        return 300 + temp[3]*10 + temp[1]
    else:
        return False

def rule8(my_arr):
    temp = []
    for i in range(5):
        temp.append(my_arr[i][1])
    temp.sort()
    if temp[0] == temp[1]:
        return 200 + temp[0]
    elif temp[1] == temp[2]:
        return 200 + temp[1]
    elif temp[2] == temp[3]:
        return 200 + temp[2]
    elif temp[3] == temp[4]:
        return 200 + temp[3]
    else:
        return False
        
if rule1(cards):
    print(rule1(cards))
elif rule2(cards):
    print(rule2(cards))
elif rule3(cards):
    print(rule3(cards))
elif rule4(cards):
    print(rule4(cards))
elif rule5(cards):
    print(rule5(cards))
elif rule6(cards):
    print(rule6(cards))
elif rule7(cards):
    print(rule7(cards))
elif rule8(cards):
    print(rule8(cards))
else:
    temp = []
    for i in range(5):
        temp.append(cards[i][1])
    print(100 + max(temp))