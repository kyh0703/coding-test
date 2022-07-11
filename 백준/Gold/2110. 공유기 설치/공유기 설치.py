import sys

input = sys.stdin.readline
N, C = map(int, input().strip().split())
house = sorted([int(input().strip()) for _ in range(N)])

low = 1
high = max(house)
mid = (low + high) // 2

def is_possible(mid):
    count = 1
    pre_i = 0
    for i in range(1, len(house)):
        if mid <= (house[i] - house[pre_i]):
            count += 1
            pre_i = i
    return C <= count

answer = 0
while low <= high:
    if is_possible(mid):
        low = mid + 1
        answer = mid
    else:
        high = mid - 1
    mid = (low + high) // 2
print(answer)