def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1]:
                basket.append(board[i][move - 1])
                board[i][move - 1] = 0
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    answer += 2
                    del basket[-2:]
                break
    return answer