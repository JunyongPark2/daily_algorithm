n, m = map(int, input().split())
def five_cnt(num):
    cnt = 0
    while num != 0:
        num //= 5
        cnt += num
    return cnt
def two_cnt(num):
    cnt = 0
    while num != 0:
        num //= 2
        cnt += num
    return cnt
print(min(five_cnt(n)-five_cnt(m)-five_cnt(n-m), two_cnt(n)-two_cnt(m)-two_cnt(n-m)))