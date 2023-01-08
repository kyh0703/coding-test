K, N, M = map(int, input().split())
sum_money = K * N
require_money = sum_money - M
print(require_money if require_money >= 0 else 0)
