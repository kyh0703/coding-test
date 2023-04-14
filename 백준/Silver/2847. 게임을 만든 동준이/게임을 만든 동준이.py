answer = 0
N = int(input())
scores = [int(input()) for _ in range(N)]

for i in range(len(scores) - 1, 0, -1):
    while scores[i-1] >= scores[i]:
        scores[i-1] -= 1
        answer += 1

print(answer)
