import sys
from collections import deque
                    
input = sys.stdin.readline
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [[-1] * m for _ in range(n)]
d = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            b[i][j] = 0
            d.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
while d:
    x, y = d.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and b[nx][ny] == -1:
                b[nx][ny] = b[x][y] + 1
                d.append((nx, ny))

for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and b[i][j] == -1:
            print(-1)
            exit(0)
print(max([max(row) for row in b]))