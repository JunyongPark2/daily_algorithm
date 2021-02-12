N, M = map(int, input().split())
chess_board = []
for _ in range(N):
    chess_board.append(list(input()))
answer = 64
for row in range(N-8+1):
    for col in range(M-8+1):
        w_cnt = 0
        b_cnt = 0
        for i in range(row, row+8):
            for j in range(col, col+8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if chess_board[i][j] == 'W':
                            b_cnt += 1
                        else:
                            w_cnt += 1
                    else:
                        if chess_board[i][j] == 'W':
                            w_cnt += 1
                        else:
                            b_cnt += 1
                else:
                    if j % 2 == 0:
                        if chess_board[i][j] == 'B':
                            b_cnt += 1
                        else:
                            w_cnt += 1
                    else:
                        if chess_board[i][j] == 'W':
                            b_cnt += 1
                        else:
                            w_cnt += 1
        if min(w_cnt, b_cnt) < answer:
            answer = min(w_cnt, b_cnt)
print(answer)