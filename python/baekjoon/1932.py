import sys

input = sys.stdin.readline

n = int(input())
a = [[0] * (n + 1) for _ in range(n + 1)]
d = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    a[i][1:i + 1] = list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + a[i][j]
print(max(d[n]))