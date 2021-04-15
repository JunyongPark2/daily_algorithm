# 벽 또ㅗ는 자기자신이랑 부딪히면 게임 끝
N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
change_dir = []
for _ in range(L):
    temp = input().split()
    change_dir.append([int(temp[0]), temp[1]])
def change(vec, s):
    if s == 'D':
        if vec == [0, 1]:
            vec = [1, 0]
        elif vec == [1, 0]:
            vec = [0, -1]
        elif vec == [0, -1]:
            vec = [-1, 0]
        elif vec == [-1, 0]:
            vec = [0, 1]
# 오른쪽 D : 아래쪽, 아래쪽 D : 왼쪽  
start = [0, 0]
end = [0, 0]
vector = [0, 1]