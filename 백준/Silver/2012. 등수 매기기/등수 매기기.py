import sys

input = sys.stdin.readline
N = int(input().strip())
expect = [int(input().strip()) for _ in range(N)]
expect.sort()

answer = 0
for i in range(N):
    answer += abs((i + 1) - expect[i])
print(answer)
