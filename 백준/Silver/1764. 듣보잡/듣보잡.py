from collections import defaultdict

N, M = map(int, input().split())
human = defaultdict(int)
for i in range(N):
    d = input()
    human[d] += 1

for i in range(M):
    s = input()
    human[s] -= 1

answer = []
for k, v in human.items():
    if v == 0:
        answer.append(k)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
