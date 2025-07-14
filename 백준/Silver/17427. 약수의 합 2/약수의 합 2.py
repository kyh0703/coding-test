N = int(input())
g = 0
for i in range(1, N + 1):
    g += i * (N // i)
print(g)
