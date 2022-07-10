import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split())
wood = list(map(int, input().strip().split()))

low = 1
high = max(wood)
mid = (low + high) // 2

def is_possible(mid):
    return M <= sum(w - mid for w in wood if mid <= w)

answer = 0
while low <= high:
    if is_possible(mid):
        low = mid + 1
        answer = mid
    else:
        high = mid - 1
    mid = (low + high) // 2
print(answer)
