N = int(input())
answer = []
for _ in range(N):
    student, apple = map(int, input().split())
    if apple // student:
        answer.append(apple % student)
    else:
        answer.append(apple)
print(sum(answer))
