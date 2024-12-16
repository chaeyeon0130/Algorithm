import sys

input = sys.stdin.readline

n = int(input())
d = [[0] * 2 for _ in range(n + 1)]
d[1][1] = 1
for i in range(2, n + 1):
    for j in range(0, 2):
        if j == 0:
            d[i][j] = d[i - 1][0] + d[i - 1][1]
        if j == 1:
            d[i][j] = d[i - 1][0]
print(d[n][0] + d[n][1])