T = int(input())
answer = [0, 0, 0]
for i in (300, 60, 10):
    while T // i:
        if i == 300:
            answer[0] += 1
        elif i == 60:
            answer[1] += 1
        elif i == 10:
            answer[2] += 1
        T = T - i

if 0 < T:
    print(-1)
else:
    print(*answer)
