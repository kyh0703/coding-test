n = int(input())
sieve = [True] * n
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i + i, n, i):
            sieve[j] = False
print([i for i in range(2, n) if sieve[i] == True])
