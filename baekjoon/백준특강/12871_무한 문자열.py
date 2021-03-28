s = input()
t = input()

# 최소단위 찾기
def least_term(my_str):
    # 문자 길이의 약수 찾기
    n = len(my_str)
    n_list = [i for i in range(1, n//2+1) if n % i == 0]
    for i in n_list:
        if my_str[:i] * (n // i) == my_str:
            return my_str[:i]
    else:
        return my_str

if least_term(s) == least_term(t):
    print(1)
else:
    print(0)