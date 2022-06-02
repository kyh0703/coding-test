a, b = map(int, input().strip().split(' '))
star = [['*'] * a for _ in range(b)]
for i in star:
    print(''.join(i))
