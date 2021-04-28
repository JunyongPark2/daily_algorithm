def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    for i in range(len(s)):
        s[i] = s[i].split(',')
        s[i] = list(map(int, s[i]))
    s.sort(key=len)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in answer:
                answer.append(s[i][j])
    return answer