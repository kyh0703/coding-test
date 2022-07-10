import sys

input = sys.stdin.readline
N = int(input().strip())
requests = list(map(int, input().strip().split()))
M = int(input().strip())

low = 0
high = max(requests)
mid = (low + high) // 2
answer = 0

def is_possible(mid):
    return sum(min(r, mid) for r in requests) <= M

while low <= high:
    if is_possible(mid):
        low = mid + 1
        answer = mid
    else:
        high = mid - 1
    mid = (low + high) // 2

print(answer)