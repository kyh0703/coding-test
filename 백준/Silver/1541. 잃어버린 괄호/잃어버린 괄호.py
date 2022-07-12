calc = input().split('-')
number = []
for i in calc:
    if '+' in i:
        number.append(sum(list(map(int, i.split('+')))))
    else:
        number.append(int(i))

answer = number[0]
for i in range(1, len(number)):
    answer -= number[i]
print(answer)