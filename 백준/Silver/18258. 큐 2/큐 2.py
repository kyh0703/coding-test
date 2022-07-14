from collections import deque
import sys
input = sys.stdin.readline

q = deque()
N = int(input().strip())
for _ in range(N):
    command = input().strip()
    if 'push' in command:
        _, v = command.split()
        q.append(v)
    elif 'pop' in command:
        print(q.popleft() if q else -1)
    elif 'size' in command:
        print(len(q))
    elif 'empty' in command:
        print(0 if q else 1)
    elif 'front' in command:
        print(q[0] if q else -1)
    elif 'back' in command:
        print(q[-1] if q else -1)