import sys
import math

input = sys.stdin.readline

n = int(input())
d = [i for i in range(0, n + 1)]
for i in range(n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        d[i] = min(d[i], d[i - j**2] + 1)
print(d[n])