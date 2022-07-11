from itertools import combinations

sieve = [True] * 3001
sieve[0] = False
sieve[1] = False
for i in range(2, 3001):
    if sieve[i] == True:
        for j in range(i + i, 3001, i):
            sieve[j] = False


def solution(nums):
    count = 0
    for i in combinations(nums, 3):
        if sieve[sum(i)]:
            count += 1
    return count