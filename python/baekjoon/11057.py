import sys

input = sys.stdin.readline

n = int(input())
d = [[0] * 10 for _ in range(n + 1)]
d[0][0] = 1
for i in range(1, n + 1):
    for j in range(10):
        for k in range(j + 1):
            d[i][j] += d[i - 1][k] % 10007
print(sum(d[n]) % 10007)