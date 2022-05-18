from inspect import stack
from queue import Queue


def solution(board, moves):
    answer = 0

    board_dict = dict()
    for col in range(len(board)):
        row_stack = []
        for row in reversed(range(len(board))):
            if board[row][col] != 0:
                row_stack.append(board[row][col])
        board_dict[col + 1] = row_stack

    basket = []
    for move in moves:
        # print(basket)
        stack = board_dict.get(move)
        if len(stack) == 0:
            continue
        top = stack.pop()
        if len(basket) == 0:
            basket.append(top)
            continue
        if basket[-1] == top:
            answer += 2
            basket.pop()
        else:
            basket.append(top)

    return answer


print("answer: ", solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]))

# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.
""" 또 하나 배워갑니다 ...
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer
 """
