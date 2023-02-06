import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    nums = input().strip()[1:-1]
    if len(nums) != 0:
        nums = nums.split(',')

    is_error, is_reverse = False, False
    for i in p:
        if i == 'R':
            if len(nums) == 0:
                continue
            is_reverse = False if is_reverse else True
        elif i == 'D':
            if len(nums) == 0:
                is_error = True
                break
            nums.pop(-1 if is_reverse else 0)

    if is_reverse:
        nums.reverse()

    if is_error:
        print('error')
    else:
        print('[', end='')
        print(*nums, sep=',', end='')
        print(']')
