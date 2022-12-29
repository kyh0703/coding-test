n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print("NO BRAINS" if x < y else "MMM BRAINS")
