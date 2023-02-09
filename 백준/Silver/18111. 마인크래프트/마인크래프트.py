import sys
input = sys.stdin.readline

N, M, B = map(int, input().strip().split())
earth = [list(map(int, input().strip().split())) for _ in range(N)]

answer = []
for current in range(257):
    time = 0
    b = B
    for i in earth:
        for j in i:
            if current == j:
                continue
            if current < j:
                diff = j - current
                time += diff * 2
                b += diff
            else:
                diff = current - j
                time += diff
                b -= diff
    if 0 <= b:
        answer.append([time, current])

answer.sort(key=lambda item: (item[0], -item[1]))
print(*answer[0])
