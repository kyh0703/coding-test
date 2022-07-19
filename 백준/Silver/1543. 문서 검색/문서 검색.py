import re

doc = input()
word = input()
p = re.compile(word)
a = p.findall(doc)
print(len(a))