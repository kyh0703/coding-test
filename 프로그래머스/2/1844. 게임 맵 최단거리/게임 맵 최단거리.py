from collections import deque

dy = (1, -1, 0, 0)
dx = (0, 0, -1, 1)

def bfs(maps, y, x):
    n = len(maps) # 세로 길이
    m = len(maps[0]) # 가로 길이

    visited = [[False] * m for _ in range(n)]
    visited[y][x] = True

    q = deque()
    q.append((y, x, 1))  # 현재 좌표와 이동 거리를 큐에 추가

    while q:
        y, x, dist = q.popleft()

        if y == n - 1 and x == m - 1:
            return dist

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny, nx, dist + 1))

    return -1

def solution(maps):
    answer = bfs(maps, 0, 0)
    return answer
