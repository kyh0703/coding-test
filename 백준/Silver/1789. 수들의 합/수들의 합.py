S = int(input())
N = 0
result = 0
for i in range(1, S + 1):
    result += i
    N += 1
    if S < result:
        N -= 1
        break
print(N)
