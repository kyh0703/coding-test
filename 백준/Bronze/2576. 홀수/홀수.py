nums = list(int(input()) for _ in range(7))

odd_nums = []
for i in nums:
    if i % 2 != 0:
        odd_nums.append(i)

if odd_nums:
    print(sum(odd_nums))
    print(min(odd_nums))
else:
    print(-1)
