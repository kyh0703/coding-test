import sys

input = sys.stdin.readline
N = int(input().strip())

def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n - 1) + f(n - 2)

print(f(N), N - 2)