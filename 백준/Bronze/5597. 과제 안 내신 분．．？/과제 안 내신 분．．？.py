nums = [int(input()) for _ in range(28)]
a = [int(i) for i in range(1, 31)]
diff_set = set(a) - set(nums)
answer = sorted(diff_set)
for i in answer:
    print(i)
