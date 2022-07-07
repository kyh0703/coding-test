import sys

N = int(sys.stdin.readline().strip())
dq = []
for _ in range(N):
    command = sys.stdin.readline().strip()
    if 'push_front' in command:
        _, v = command.split(' ')
        dq.insert(0, v)
    elif 'push_back' in command:
        _, v = command.split(' ')
        dq.append(v)
    elif 'pop_front' == command:
        print(-1 if len(dq) == 0 else dq.pop(0))
    elif 'pop_back' == command:
        print(-1 if len(dq) == 0 else dq.pop(-1))
    elif 'size' == command:
        print(len(dq))
    elif 'empty' == command:
        print(1 if len(dq) == 0 else 0)
    elif 'front' == command:
        print(-1 if len(dq) == 0 else dq[0])
    elif 'back' == command:
        print(-1 if len(dq) == 0 else dq[-1])