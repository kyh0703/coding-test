T = int(input())
for _ in range(T):
    N = int(input())
    stocks_price = list(map(int, input().split()))
    answer = 0
    max_price = 0
    for i in stocks_price[::-1]:
        if max_price <= i:
            max_price = i
            continue
        answer += max_price - i
    print(answer)