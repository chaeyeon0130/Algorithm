# 탐색 두 번
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    a[u].append((v, w))
    a[v].append((u, w))
    
def bfs(start):
    dist = [-1] * (n + 1)
    check = [0] * (n + 1)
    q = deque()
    
    check[start] = 1
    dist[start] = 0
    q.append(start)
    while q:
        x = q.popleft()
        for to, cost in a[x]:
            if check[to] == 0:
                dist[to] = dist[x] + cost
                check[to] = 1
                q.append(to)
    
    return dist

dist = bfs(1)
start = 1
for i in range(2, n + 1):
    if dist[i] > dist[start]:
        start = i

dist = bfs(start)
ans = max(dist[1:])

print(ans)