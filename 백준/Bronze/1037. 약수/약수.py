N = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)
print(min(nums) * max(nums))
