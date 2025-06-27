import sys

input = sys.stdin.readline
answer = []
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    base = a % 10
    if base == 0:
        answer.append(10)
    elif base == 1 or base == 5 or base == 6:
        answer.append(base)
    elif base == 4 or base ==  9:
        if b % 2 == 0:
            answer.append((base ** 2) % 10)
        else:
            answer.append(base)
    else:
        if b % 4 == 0:
            answer.append((base ** 4) % 10)
        else:
            answer.append((base ** (b % 4)) % 10)


print(*answer, sep='\n')
