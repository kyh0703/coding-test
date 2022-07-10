import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N = int(input().strip())
own_card = sorted(map(int, input().strip().split()))
M = int(input().strip())
find_card = map(int, input().strip().split())

answer = []
for i in find_card:
    answer.append(bisect_right(own_card, i) - bisect_left(own_card, i))
print(*answer)
