n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# n 배열의 크기
# m 더할 숫자
# k 연속해서 더할 숫자
print(n, m, k)
print(data)
data.sort()
first = data[n - 1]
second = data[n - 2]
print(first)
print(second)

answer = 0
continue_count = 0
while m != 0:
    if continue_count < k:
        answer += first
    else:
        answer += second
    if continue_count == k:
        continue_count = 0
    continue_count += 1
    m -= 1

print(answer)
