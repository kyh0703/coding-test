T = int(input())
k = []
n = []

apartment = [[0 for _ in range(15)] for _ in range(15)]
for i in range(1, 15):
    apartment[0][i] = i

for y in range(1, 15):
    for x in range(1, 15):
        apartment[y][x] = apartment[y-1][x] + apartment[y][x-1]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(apartment[k][n])
