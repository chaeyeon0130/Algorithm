import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy= [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(n):
    l = int(input())
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    chess = [[-1] * l for _ in range(l)]
    d = deque()

    chess[a1][b1] = 0
    d.append((a1, b1))
    while d:
        x, y = d.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == -1:
                chess[nx][ny] = chess[x][y] + 1
                d.append((nx, ny))
    
    print(chess[a2][b2])