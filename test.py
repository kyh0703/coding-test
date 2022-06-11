def solution(arr, n, m):
    answer = 0
    divide = n//m
    row_sum = dict()
    for row in range(n):
        for i in range(divide, n, divide):
            prev = row_sum.get(row, arr[row][i-i:i])
            tail = reversed(arr[row][i:i+i])
            sum = [x + y for x, y in zip(prev, tail)]
            row_sum[row] = sum
            if answer < max(sum):
                answer = max(sum)
    return answer


print(solution([
    [5, 1, 8, 2, 3, 3],
    [6, 5, 2, 1, 3, 3],
    [1, 1, 5, 6, 3, 3],
    [1, 1, 1, 1, 3, 3],
    [1, 1, 1, 1, 3, 3],
    [1, 1, 1, 1, 3, 3],
], 6, 3))
