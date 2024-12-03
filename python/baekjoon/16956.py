import sys

input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ok = True
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < r and 0 <= y < c:
                    if arr[x][y] == 'W':
                        ok = False

if not ok:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                print('D', end = '')
            else:
                print(arr[i][j], end = '')
        print()