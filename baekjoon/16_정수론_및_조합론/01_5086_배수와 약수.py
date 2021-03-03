while True:
    first, second = map(int, input().split())
    if first == 0 and second == 0:
        break
    if second % first == 0:
        print('factor')
    elif first % second == 0:
        print('multiple')
    else:
        print('neither')