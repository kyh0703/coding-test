import sys

line = sys.stdin.read()
line = line.replace('\n', '').replace(' ', '')

count_dict = dict()
for i in line:
    count_dict[i] = count_dict.get(i, 0) + 1
sort_dict = sorted(count_dict.items(),
                   key=lambda item: item[1], reverse=True)
max_value = 0
answer = []
for i in sort_dict:
    char, count = i
    if max_value <= count:
        answer.append(char)
        max_value = count
answer.sort()
print(''.join(answer))
