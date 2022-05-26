array = []


def solution(home):
    pos_y = 1
    pos_x = 1

    while True:
        next_x = home[pos_y][pos_x + 1]
        if next_x == 0:
            home[pos_y][pos_x] = 9
            pos_x += 1
            continue
        elif next_x == 2:
            home[pos_y][pos_x] = 9
            home[pos_y][pos_x + 1] = 9
            break

        next_y = home[pos_y + 1][pos_x]
        if next_y == 0:
            home[pos_y][pos_x] = 9
            pos_y += 1
            continue
        elif next_y == 2:
            home[pos_y][pos_x] = 9
            home[pos_y + 1][pos_x] = 9
            break

        if next_x == 1 and next_y == 1:
            break

    for i in home:
        for j in i:
            print(j, end=' ')
        print()

for i in range(10):
    array.append(list(map(int, input().split())))

solution(array)



# ant_home = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#             [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
#             [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
#             [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# print(solution(ant_home))
