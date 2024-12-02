import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dist = [[-1] * n for _ in range(n)]
queue = deque()

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
dist[r1][c1] = 0
queue.append((r1, c1))
while queue:
    x, y = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if dist[nx][ny] == -1:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
print(dist[r2][c2])