n, m = map(int, input().split())
# n = 행의 개수
# m = 열의 개수

for row in n:
    data = list(map(int, input().split))
    min_value = min(data)
    result = max(result, min_value)

print(result)
