from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        nx, ny = q.popleft()
        # 방향을 살핀다
        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue
            if maps[xx][yy] == 0:
                continue
            if maps[xx][yy] == 1:
                maps[xx][yy] = maps[nx][ny] + 1
                print(nx, ny, maps[nx][ny])
                q.append((xx, yy))

    return maps[n - 1][m-1]


def dfs(x, y, value):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if maps[x][y] == 0:
        return

    if maps[x][y] == 1:
        value += 1
    else:
        value -= 1
    print(x, y)
    if x == n - 1 and y == m - 1:
        return

    dfs(x + 1, y, value)
    dfs(x, y + 1, value)
    dfs(x - 1, y, value)
    dfs(x, y - 1, value)


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# n, m = map(int, input().split())
# maps = []
# for i in range(n):
#     maps.append(list(map(int, input())))

n, m = 4, 6
maps = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
]
# print(bfs(0, 0))
print(dfs(0, 0, 0))
