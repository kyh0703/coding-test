N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]
for test_case in T:
    r, e, c = test_case
    profit = e - c
    if r < profit:
        print('advertise')
    elif r == profit:
        print('does not matter')
    else:
        print('do not advertise')
