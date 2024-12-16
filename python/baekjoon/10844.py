import sys

input = sys.stdin.readline

n = int(input())
d = [[0] * 10 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(0, 10):
        if i == 1 and j != 0:
            d[i][j] = 1
        elif j == 0:
            d[i][j] = d[i - 1][j + 1]
        elif j == 9:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]
print(sum(d[n]) % 1000000000)