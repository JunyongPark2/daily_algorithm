N, K = map(int, input().split())
A = list(map(int, input().split()))

# K를 소인수 분해하자
K_clone = K

# 소수 구하기 (위키피디아 참조 https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

K_dict = {}
for i in prime_list(K_clone):
    while True:
        if K_clone >= i and K_clone % i == 0:
            K_clone //= i
            K_dict[i] = K_dict.get(i, 0) + 1
        else:
            break
    if K_clone == 1:
        break
# print(K_dict)


# A의 원소들은 K의 소인수들의 갯수를 세자.
A_list = []
x = 0
for a in A:
    # a_dict = {i:0 for i in K_dict.keys()}
    a_list = [0 for _ in K_dict.keys()]
    # for i in a_dict.keys():
    for i in range(len(a_list)):
        while True:
            if a >= list(K_dict.keys())[i] and a % list(K_dict.keys())[i] == 0:
                a //= list(K_dict.keys())[i]
                # a_dict[i] += 1
                a_list[i] += 1
                if a_list[i] == list(K_dict.values())[i]:
                    break
            else:
                break
    # 하나가 바로 만족하는거 갯수 세고 제외
    if a_list == list(K_dict.values()):
        x += 1
    # 모두 0인건 리스트에서 제외
    elif sum(a_list) != 0:
        A_list.append(a_list)
cnt = 0
def comb(n):
    if N == n:
        return 1
    temp = 0
    for i in range(n):
        temp += (N-(n+1))*(N-(n+2))//2
    return temp

cnt += comb(x)
# A_list = sorted(A_list, key=lambda x: [-x[i] for i in range(len(A_list[0]))])
# print(A_list)



K_list = list(K_dict.values())
# print(K_list)

# 만족하는지 함수 정의
def my_func(a, b):
    for i in range(len(a)):
        if a[i] < b[i]:
            return False
    else:
        return True

# 리스트 합 구하기
def list_sum(a, b):
    temp = []
    for i in range(len(a)):
        temp.append(a[i] + b[i])
    return temp

# 중간에 만족하면 멈추는걸 해야할거같음.
for p in range(len(A_list)-2):
    for q in range(p+1, len(A_list)-1):
        for r in range(q+1, len(A_list)):
            if my_func(list_sum(A_list[p],list_sum(A_list[q], A_list[r])), K_list):
                cnt += 1

# # 중간에 만족하면 멈추는걸 해야할거같음.
# for p in range(len(A_list)-2):
#     temp = A_list[p]
#     if my_func(temp, K_list):
#         cnt += (N-1-p)*(N-1-p-1)//2
#     else:
#         for q in range(p+1, len(A_list)-1):
#             temp1 = list_sum(temp, A_list[q])
#             if my_func(temp1, K_list):
#                 cnt += N-1-q
#             else:
#                 for r in range(q+1, len(A_list)):
#                     temp2 = list_sum(temp1, A_list[r])
#                     if my_func(temp2, K_list):
#                         cnt += 1
print(cnt)