import sys
from collections import deque

input = sys.stdin.readline
q = deque()

n = int(input())
a = [[] for _ in range(n)]
check = [False] * n
parent = [-1] * n

for _ in range(n - 1):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

order = list(map(lambda x: int(x) - 1, input().split()))

m = 1
q.append(0)
check[0] = True
for i in range(n):
    x = q.popleft()
    if x != order[i]:
        print(0)
        exit(0)
    cnt = 0
    for y in a[x]:
        if check[y] == False:
            parent[y] = x
            cnt += 1
    for j in range(cnt):
        if m + j >= n or parent[order[m + j]] != x:
            print(0)
            exit(0)
        q.append(order[m + j])
        check[order[m + j]] = True
    m += cnt
print(1)