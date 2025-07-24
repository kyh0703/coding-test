T = int(input())
for _ in range(T):
    answer = []
    C = int(input())
    for i in (25, 10, 5, 1):
        answer.append(C // i)
        C %= i
    print(*answer)
