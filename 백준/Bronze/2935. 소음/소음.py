A = int(input())
operator = input()
B = int(input())

answer = 0
if operator == '+':
    answer = A + B
elif operator == '*':
    answer = A * B

print(answer)