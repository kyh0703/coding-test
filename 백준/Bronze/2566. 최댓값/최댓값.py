maps = []
for _ in range(9):
    maps.append(list(map(int, input().split())))

max_value = -1
pos = []
for i in range(9):
    for j in range(9):
        if maps[i][j] > max_value:
            max_value = maps[i][j]
            pos = [i + 1, j + 1]

print(max_value)
print(*pos)
