while True:
    first, second = map(int, input().split())
    if first == 0 and second == 0:
        break
    print("Yes" if first > second else "No")
