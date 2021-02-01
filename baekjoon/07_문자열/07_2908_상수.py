A, B = input().split()
# 문자열 뒤집기 A[::-1] or for문돌리기 or ''.join(reversed(A))
if int(A[::-1]) > int(B[::-1]):
    print(A[::-1])
else:
    print(B[::-1])