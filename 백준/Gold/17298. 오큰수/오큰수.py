N = int(input())
A = list(map(int, input().split()))
answer = []
stack = []
for i in range(N - 1, -1, -1):
    while stack and stack[-1] <= A[i]:
        stack.pop()
    if stack:
        answer.append(stack[-1])
    else:
        answer.append(-1)
    stack.append(A[i])
answer.reverse()
print(*answer)