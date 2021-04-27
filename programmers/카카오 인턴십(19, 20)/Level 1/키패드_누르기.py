def trans(number):
    if number == 0:
        return 3, 1
    row = (number-1) // 3
    col = (number-1) % 3
    return [row, col]

def dist(list1, list2):
    return abs(list1[0]-list2[0]) + abs(list1[1]-list2[1])

def solution(numbers, hand):
    answer = ''
    cur_left = [3, 0]
    cur_right = [3, 2]
    for number in numbers:
        trans_number = trans(number)
        if trans_number[1] == 0:
            cur_left = trans_number
            answer += 'L'
        elif trans_number[1] == 2:
            cur_right = trans_number
            answer += 'R'
        else:
            dist_L = dist(cur_left, trans_number)
            dist_R = dist(cur_right, trans_number)
            if dist_L > dist_R:
                cur_right = trans_number
                answer += 'R'
            elif dist_L < dist_R:
                cur_left = trans_number
                answer += 'L'
            else:
                if hand == 'left':
                    cur_left = trans_number
                    answer += 'L'
                else:
                    cur_right = trans_number
                    answer += 'R'
    return answer