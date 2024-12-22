import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = [0] * n
id = [0] * n
d[0] = a[0]
for i in range(1, n):
    d[i] = a[i]
    if d[i - 1] + a[i] > d[i]:
        d[i] = d[i - 1] + a[i]

id[n - 1] = a[n - 1]
for i in reversed(range(n - 1)):
    id[i] = a[i]
    if id[i + 1] + a[i] > id[i]:
        id[i] = id[i + 1] + a[i]

result = max(d)
for i in range(1, n - 1):
    result = max(result, d[i - 1] + id[i + 1])
print(result)