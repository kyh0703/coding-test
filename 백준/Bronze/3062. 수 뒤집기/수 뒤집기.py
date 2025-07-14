T = int(input())
for i in range(T):
    N = input()
    sum_value = int(N) + int(N[::-1])
    print("YES" if str(sum_value) == str(sum_value)[::-1] else "NO")