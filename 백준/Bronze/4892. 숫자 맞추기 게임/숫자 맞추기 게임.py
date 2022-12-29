count = 0
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = n0 * 3
    n2 = n1 // 2 if n1 % 2 == 0 else (n1 + 1) // 2
    n3 = n2 * 3
    n4 = n3 // 9
    count += 1

    if n1 % 2 == 0:
        print(f'{count}. even {n4}')
    else:
        print(f'{count}. odd {n4}')
