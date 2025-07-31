import math

def get_division(n: int) -> list:
    division = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            division.append(i)
            if i != n // i:
                division.append(n // i)
    return division

N, K = map(int, input().split())
division = get_division(N)
division.sort()
if len(division) < K:
    print(0)
else:
    print(division[K - 1])
