import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N = int(input().strip())
numbers = sorted(map(int, input().strip().split()))
M = int(input().strip())
find_numbers = map(int, input().strip().split())

def is_exist(target):
    return 1 <= (bisect_right(numbers, target) - bisect_left(numbers, target))

answer = []
for i in find_numbers:
    answer.append(1 if is_exist(i) else 0)
for i in answer:
    print(i)
