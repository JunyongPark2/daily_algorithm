def solution(gems):
    n = len(set(gems))
    answer = [0, len(gems)-1]
    my_dict = {gems[0]: 1}
    start, end = 0, 0

    while start < len(gems) and end < len(gems):
        if len(my_dict) == n:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            if my_dict[gems[start]] == 1:
                del my_dict[gems[start]]
            else:
                my_dict[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in my_dict.keys():
                my_dict[gems[end]] += 1
            else:
                my_dict[gems[end]] = 1
    answer[0] += 1
    answer[1] += 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

