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
            if check[i] == 0:
                sel[idx] = arr[i] # 값을 써라
                check[i] = 1 # 사용을 했다는 표시
                perm(idx + 1)
                check[i] = 0 # 다음 반복문을 위한 원상복구

perm(0)