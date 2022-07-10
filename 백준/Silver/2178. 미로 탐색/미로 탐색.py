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
                q.append((xx, yy))

    return maps[n - 1][m-1]


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input())))

print(bfs(0, 0))
