import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [0] * n
for i in range(0, n):
    d[i] = arr[i]
    if d[i] < d[i - 1] + arr[i]:
        d[i] = d[i - 1] + arr[i]
print(max(d))