import sys

input = sys.stdin.readline
stack = []
N = int(input().strip())
for _ in range(N):
    K = int(input().strip())
    if K == 0:
        stack.pop(-1)
    else:
        stack.append(K)
print(sum(stack))