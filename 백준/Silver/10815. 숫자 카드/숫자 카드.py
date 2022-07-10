import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N = int(input().strip())
own_cards = list(map(int, input().strip().split()))
M = int(input().strip())
find_cards = list(map(int, input().strip().split()))


def is_exist(target):
    return 1 <= (bisect_right(own_cards, target) - bisect_left(own_cards, target))

answer = []
own_cards.sort()
for i in find_cards:
    answer.append(1 if is_exist(i) else 0)

for i in answer:
    print(i, end=' ')
