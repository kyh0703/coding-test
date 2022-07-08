import re

regex = re.compile(r'(<.*?>)|(\w+)|(\s)')
result = regex.findall(input())
for tag, str, space in result:
    print(tag + str[::-1] + space, end='')