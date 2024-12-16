import sys

input = sys.stdin.readline

d = [[0] * 4 for _ in range(100001)]
for i in range(1, 100001):
    for j in range(1, 4):
        if i == j:
            d[i][j] = 1
        elif j == 1 and i >= 1:
            d[i][1] = (d[i - 1][2] + d[i - 1][3]) % 1000000009
        elif j == 2 and i >= 2:
            d[i][2] = (d[i - 2][1] + d[i - 2][3]) % 1000000009
        elif j == 3 and i >= 3:
            d[i][3] = (d[i - 3][1] + d[i - 3][2]) % 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    print((d[n][1] + d[n][2] + d[n][3]) % 1000000009)