import sys
input = sys.stdin.readline


def bracket(string):
    i = 0
    stack = []
    while string[i] != ".":
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])
        elif string[i] == ')':
            if len(stack) == 0 or stack.pop(-1) != '(':
                return "no"
        elif string[i] == ']':
            if len(stack) == 0 or stack.pop(-1) != '[':
                return "no"
        i += 1
    return 'yes' if len(stack) == 0 else 'no'


while True:
    line = input().rstrip()
    if line == '.':
        break
    print(bracket(line))
