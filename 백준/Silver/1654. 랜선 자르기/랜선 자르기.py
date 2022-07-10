import sys

input = sys.stdin.readline
K, N = map(int, input().strip().split())
lines = [int(input()) for _ in range(K)]

low = 1
high = max(lines)
mid = (low + high) // 2

def is_possible(mid):
    return N <= sum(line // mid for line in lines)

answer = 0
while low <= high:
    if is_possible(mid):
        low = mid + 1
        answer = mid
    else:
        high = mid - 1
    mid = (low + high) // 2
print(answer)
