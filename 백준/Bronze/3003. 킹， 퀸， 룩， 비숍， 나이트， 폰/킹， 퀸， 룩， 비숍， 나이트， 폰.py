chess = [1, 1, 2, 2, 2, 8]
inputs = list(map(int, input().split()))
answer = []
for b, w in zip(chess, inputs):
    answer.append(0 if b == w else b - w)
print(*answer)