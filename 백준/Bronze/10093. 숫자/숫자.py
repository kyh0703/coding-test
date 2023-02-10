A, B = map(int, input().split())
print(0 if A == B else abs(B - A) - 1)
if A < B:
    print(*sorted(list(range(A + 1, B))))
else:
    print(*sorted(list(range(B + 1, A))))
