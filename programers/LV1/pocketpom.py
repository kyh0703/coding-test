def solution(nums):
    kind = dict()
    for monster in nums:
        kind[monster] = kind.get(monster, 0) + 1

    n = len(nums) / 2
    answer = 0
    if n < len(kind):
        answer = n
    else:
        answer = len(kind)
    return int(answer)


print("answer", solution([3, 1, 2, 3]))
print("answer", solution([3, 3, 3, 2, 2, 4]))
print("answer", solution([3, 3, 3, 2, 2, 2]))


# def solution(ls):
# return min(len(ls)/2, len(set(ls)))
