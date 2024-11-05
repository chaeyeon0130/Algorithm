import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    board = [[0] * m for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            board[i][j] = arr[i][j]
            if board[i][j] == 2:
                queue.append((i, j))
                
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    queue.append((nx, ny))
    
    safe = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                safe += 1    
    return safe

ans = 0
def make_wall(count):
    global ans
    if count == 3:
        safe = bfs()
        if ans < safe: ans = safe
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make_wall(count + 1)
                arr[i][j] = 0

make_wall(0)
print(ans)