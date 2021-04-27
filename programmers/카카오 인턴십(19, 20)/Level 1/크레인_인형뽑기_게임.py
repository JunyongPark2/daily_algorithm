def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    for move in moves:
        for row in range(N):
            if board[row][move-1]:
                stack.append(board[row][move-1])
                board[row][move-1] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer