N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))
operator_list = ['+'] * operator[0] + ['-'] * operator[1] + ['*'] * operator[2] + ['/'] * operator[3]
sel = [0] * len(operator_list) # 뽑은 결과를 적음
check = [0] * len(operator_list) # 해당 원소를 이미 사용했는지 안했는지에 대한 체크

perm_list = []
def perm(idx):
    # 다 뽑아서 정리했다면
    if idx == len(operator_list):
        # 리스트를 바꾸면 perm_list안에 내용도 바뀌어서 copy()로 복사본을 붙혀넣기
        perm_list.append(sel.copy())
    else:
        for i in range(len(operator_list)):
            if check[i] == 0:
                sel[idx] = operator_list[i] # 값을 써라
                check[i] = 1 # 사용을 했다는 표시
                perm(idx + 1)
                check[i] = 0 # 다음 반복문을 위한 원상복구

perm(0)
max_value = -1000000001
min_value = 1000000001
for case in perm_list:
    value = A[0]
    for i in range(N-1):
        if case[i] == '+':
            value += A[i+1]
        elif case[i] == '-':
            value -= A[i+1]
        elif case[i] == '*':
            value *= A[i+1]
        elif case[i] == '/':
            if value < 0:
                value = -(-value // A[i+1])
            else:
                value //= A[i+1]
    if value < min_value:
        min_value = value
    if value > max_value:
        max_value = value
print(max_value)
print(min_value)
