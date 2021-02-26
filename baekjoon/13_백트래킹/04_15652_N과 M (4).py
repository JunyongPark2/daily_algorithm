N, M = map(int, input().split())
sel = [0] * M # 결과들이 저장될 리스트
check = [0] * N # 해당 원소를 이미 사용했는지 안했는지에 대한 체크
arr = list(range(1, N+1))

def perm(idx):
    # 다 뽑아서 정리했다면
    if idx == M:
        print(*sel)
    else:
        for i in range(N):
            if check[i] == 0 and (idx == 0 or arr[i] >= sel[idx-1]):
                sel[idx] = arr[i] # 값을 써라
                perm(idx + 1)

perm(0)