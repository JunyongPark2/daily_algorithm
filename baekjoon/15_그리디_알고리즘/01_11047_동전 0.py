N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.reverse()
cnt = 0
# 동전의 가치 a들이 모두 배수관계에 있기에 이렇게 해도 됨.
# 시간 초과
# for a in A:
#     while K >= a:
#         K -= a
#         cnt += 1
# print(cnt)

# 나눗셈으로 가능할듯
for a in A:
    cnt += K // a
    K = K % a
print(cnt)