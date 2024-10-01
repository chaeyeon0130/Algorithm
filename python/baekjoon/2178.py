import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(i, j):
    d = deque()
    count = 1
    b[i][j] = count
    d.append((i, j))
    while d:
        x, y = d.popleft()
        count = b[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and b[nx][ny] == 0:
                    b[nx][ny] = count
                    d.append((nx, ny))
                
bfs(0, 0)
print(b[n - 1][m - 1]) 