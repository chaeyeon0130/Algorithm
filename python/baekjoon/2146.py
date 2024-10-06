import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
g = [[0] * n for _ in range(n)]

count = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque()
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and g[i][j] == 0:
            count += 1
            q.append((i, j))
            g[i][j] = count
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny] == 1 and g[nx][ny] == 0:
                            g[nx][ny] = g[x][y]
                            q.append((nx, ny))

q = deque()
d = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            d[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                g[nx][ny] = g[x][y]
                q.append((nx, ny))
            # if d[nx][ny] > 0:
            #     if d[x][y] > 0:
            #         if g[nx][ny] != g[x][y]:
            #             if ans == 0  or ans > d[nx][ny] + d[x][y]:
            #                 ans = d[nx][ny] + d[x][y]

ans = -1
for i in range(n):
    for j in range(n):
        for k in range(4):
            x, y = i+dx[k], j+dy[k]
            if 0 <= x < n and 0 <= y < n:
                if g[i][j] != g[x][y]:
                    if ans == -1 or ans > d[i][j] + d[x][y]:
                        ans = d[i][j] + d[x][y]    
print(ans)