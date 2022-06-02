def dfs(h, x, y) -> bool:
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if maps[x][y] <= h:
        visited[x][y] = True
        return False
    if visited[x][y]:
        return False
    visited[x][y] = True
    dfs(h, x - 1, y)
    dfs(h, x + 1, y)
    dfs(h, x, y - 1)
    dfs(h, x, y + 1)
    return True


n = int(input())
visited = [[False] * n for _ in range(n)]
print(visited)
maps = [[0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [
    0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]
# for i in range(n):
#     maps.append(list(map(int, input().split())))

count = 0
for i in range(n):
    for j in range(n):
        if dfs(1, 0, 0):
            count += 1

# print(count)
