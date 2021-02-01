T = input().lower()
if len(T) == 1:
    print(T.upper())
else:
    my_dict = {}
    # SSAFY 수업시간에 배운 count안쓰고 딕셔너리에 갯수 저장하는거
    for i in T:
        my_dict[i] = my_dict.get(i, 0) + 1
    # 정렬 조건에 lambda 표현식 사용
    result = sorted(my_dict.items(), key = lambda x: x[1], reverse=True)

    if result[0][1] == result[1][1]:
        print('?')
    else:
        print(result[0][0].upper())