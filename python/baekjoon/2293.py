import sys

input = sys.stdin.readline
n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
d = [0] * (k + 1)
d[0] = 1

for i in range(n):
    for j in range(money[i], k + 1):
        d[j] = d[j] + d[j - money[i]]
print(d[k])
