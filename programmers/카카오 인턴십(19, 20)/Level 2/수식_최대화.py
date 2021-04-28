def cal(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '+':
        temp = eval('+'.join([cal(priority, n+1, e) for e in expression.split('+')]))
    elif priority[n] == '-':
        temp = eval('-'.join([cal(priority, n+1, e) for e in expression.split('-')]))
    elif priority[n] == '*':
        temp = eval('*'.join([cal(priority, n+1, e) for e in expression.split('*')]))
    return str(temp)

def solution(expression):
    answer = 0
    priorities = [
        ('+', '-', '*'),
        ('+', '*', '-'),
        ('-', '+', '*'),
        ('-', '*', '+'),
        ('*', '+', '-'),
        ('*', '-', '+'),
    ]
    for priority in priorities:
        temp = abs(int(cal(priority, 0, expression)))
        answer = max(answer, temp)
    return answer

print(solution("100-200*300-500+20"))