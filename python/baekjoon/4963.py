import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
def dfs(i, j):
    check[i][j] = True
    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < h and 0 <= ny < w:
            if a[nx][ny] == 1 and check[nx][ny] == False:
                dfs(nx, ny)
    
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    a = [list(map(int, input().split())) for _ in range(h)]
    check = [[False] * w for _ in range(h)]
    
    island = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1 and check[i][j] == False:
                island += 1
                dfs(i, j)
    
    print(island)