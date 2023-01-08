scores = [int(input()) for _ in range(5)]
total = 0
for i in scores:
    total += 40 if i < 40 else i
print(total // 5)
