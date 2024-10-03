import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
check = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y, cnt, color):
    if check[x][y]:
        if cnt - dist[x][y] >= 4:
            return True
        else:
            return False
    check[x][y] = True
    dist[x][y] = cnt
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == color:
            if dfs(nx, ny, cnt + 1, color):
                return True
    return False

for i in range(n):
    for j in range(m):
        if not check[i][j]:
            # dist = [[0] * m for _ in range(n)]
            exist = dfs(i, j, 1, a[i][j])
            if exist:
                print('Yes')
                exit(0)
print('No')