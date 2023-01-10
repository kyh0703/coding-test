N = int(input())
nums = list(map(int, input().split()))
V = int(input())

num_dict = dict()
for i in nums:
    num_dict[i] = num_dict.get(i, 0) + 1

print(num_dict.get(V, 0))
