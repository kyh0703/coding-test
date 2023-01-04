gathers = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')

while True:
    line = input()
    if line == '#':
        break
    count = 0
    for i in line:
        if i in gathers:
            count += 1
    print(count)
