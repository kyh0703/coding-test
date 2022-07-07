a, b = map(int, input().split())


def GCD(a, b):
    r = a % b
    if r == 0:
        return b
    return GCD(b, r)


print(GCD(a, b))
print((a * b) // GCD(a, b))
