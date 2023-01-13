n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0

for x, y in points:
    if x == 0 or y == 0:
        axis += 1
        continue

    if x > 0:
        if y > 0:
            q1 += 1
        else:
            q4 += 1
    else:
        if y > 0:
            q2 += 1
        else:
            q3 += 1

print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {axis}')
