import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if arr[nx][ny] == 1:
                arr[nx][ny] = -1
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split()) # m : 가로 길이, n : 세로 길이
    arr = [[0] * m for _ in range(n)]
    result = 0

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = -1
                dfs(i, j)
                result += 1

    print(result)