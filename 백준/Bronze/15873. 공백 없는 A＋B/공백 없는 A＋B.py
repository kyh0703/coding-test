import re

a = input()
answer = 0
regex = re.findall('10', a)
answer = len(regex) * 10
a = a.replace('10', '')

for i in a:
    answer += int(i)
print(answer)
