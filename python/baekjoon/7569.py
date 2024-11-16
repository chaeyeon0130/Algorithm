import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dist = [[[-1] * m for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if arr[nz][nx][ny] == 0 and dist[nz][nx][ny] == -1:
                    dist[nz][nx][ny] = dist[z][x][y] + 1
                    queue.append((nz, nx, ny))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                dist[i][j][k] = 0
                queue.append((i, j, k))
bfs()

ans = 0
exception = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0 and dist[i][j][k] == -1:
                exception = True
            ans = max(ans, dist[i][j][k])

if exception:
    print(-1)
elif ans > 0:
    print(ans)
elif ans == 0:
    print(ans)