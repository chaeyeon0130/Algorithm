import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
q = deque() # 현재 큐
next_q = deque() # 다음 큐

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q.append((0, 0))
check[0][0] = 1
while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == 0:
                if a[nx][ny] == 0:
                    check[nx][ny] = 1
                    dist[nx][ny] = dist[x][y]
                    q.append((nx, ny))
                else:
                    check[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    next_q.append((nx, ny))
    
    if not q:
        q = next_q
        next_q = deque()

print(dist[n - 1][m - 1])