line = input()
answer = []
for i in line:
    if i.isupper():
        answer.append(i.lower())
    elif i.islower():
        answer.append(i.upper())
    else:
        answer.append(i)
print(''.join(answer))
