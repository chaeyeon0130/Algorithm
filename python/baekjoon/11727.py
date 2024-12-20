import sys

input = sys.stdin.readline

d = [0] * 1001
d[0] = d[1] = 1

n = int(input())

for i in range(2, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 10007
print(d[n])