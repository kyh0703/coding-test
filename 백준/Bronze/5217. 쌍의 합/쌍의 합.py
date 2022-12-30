from itertools import combinations

test_case = int(input())
for _ in range(test_case):
    pairs = []
    n = int(input())
    for i in combinations(range(n), 2):
        if sum(i) == n:
            pairs.append(i)

    print(f'Pairs for {n}:', end=' ')
    for i in range(len(pairs)):
        first, second = pairs[i]
        if i != len(pairs) - 1:
            print(f'{first} {second},', end=' ')
        else:
            print(f'{first} {second}', end='')
    print()
