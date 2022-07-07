from itertools import combinations

t = int(input())
for _ in range(t):
    line = list(map(int, input().split()))
    n = line[0]
    gcd_list = line[1:]
    answer = 0
    for a, b in combinations(gcd_list, 2):
        for j in range(min(a, b), 0, -1):
            if a % j == 0 and b % j == 0:
                answer += j
                break
    print(answer)
