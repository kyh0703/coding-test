N = int(input())
distance = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

pos = oil_price[0]
answer = pos * distance[0]
for i in range(1, N - 1):
    if oil_price[i] < pos:
        pos = oil_price[i]
    answer += pos * distance[i]
print(answer)