import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    d = [[0] * 3 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(3):
            if j == 0:
                d[i][j] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])
            elif j == 1:
                d[i][j] = max(d[i - 1][0], d[i - 1][2]) + arr[0][i - 1]
            elif j == 2:
                d[i][j] = max(d[i - 1][0], d[i - 1][1]) + arr[1][i - 1]
    print(max(d[n]))