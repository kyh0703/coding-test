def GCD(a, b):
    r = a % b
    if r == 0:
        return b
    return GCD(b, r)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print((A * B) // GCD(A, B))
