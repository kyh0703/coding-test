N = int(input())
for i in range(1, N + 1):
    spaces = ' ' * (N - i)
    starts = '*' * (2 * i - 1)
    print(spaces + starts)

for i in range(N - 1, 0, -1):
    spaces = ' ' * (N - i)
    starts = '*' * (2 * i - 1)
    print(spaces + starts)
