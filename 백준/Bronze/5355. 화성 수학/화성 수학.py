T = int(input())
for _ in range(T):
    test_case = map(str, input().split())
    answer = 0.0
    for i in test_case:
        if i == '@':
            answer *= 3
        elif i == '%':
            answer += 5
        elif i == '#':
            answer -= 7
        else:
            answer += float(i)
    print(f'{answer:.2f}')
