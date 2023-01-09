bowls = input()
last_position = dict()
answer = 0
for i, v in enumerate(bowls):
    last = last_position.get(v)
    if last == None:
        answer += 10
    elif last == i - 1:
        answer += 5
    else:
        answer += 10
    last_position[v] = i
print(answer)
