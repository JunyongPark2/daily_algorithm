import math
def solution(w,h):
    total = w * h
    answer = total - (w + h - math.gcd(w,h))
    return answer