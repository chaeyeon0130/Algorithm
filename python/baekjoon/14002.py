import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [1] * n
v = [-1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            v[i] = j

print(max(d))
# 재귀 써도 됨
idx = d.index(max(d))
lst = []
lst.append(arr[idx])
idx = v[idx]
while idx != -1:
    lst.append(arr[idx])
    idx = v[idx]
lst.reverse()
print(' '.join(list(map(str, lst))))