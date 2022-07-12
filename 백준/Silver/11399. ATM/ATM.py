N = int(input())
PS = sorted(list(map(int, input().split())))
answer = [0]
for i in range(len(PS)):
    answer.append(answer[-1] + PS[i])
print(sum(answer))