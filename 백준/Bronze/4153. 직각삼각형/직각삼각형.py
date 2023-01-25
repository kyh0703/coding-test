while True:
    nums = sorted(list(map(int, input().split())))
    A, B, C = nums
    if A == 0 and B == 0 and C == 0:
        break
    if A ** 2 + B ** 2 == C ** 2:
        print('right')
    else:
        print('wrong')
