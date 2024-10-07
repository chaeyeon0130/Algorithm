import sys
from collections import deque

input = sys.stdin.readline
q = deque()

MAX = 200000
n, k = map(int, input().split())
check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)

check[n] = True
dist[n] = 0
q.append(n)
while q:
    now = q.popleft()
    
    if now - 1 >= 0:
        if not check[now - 1]:
            q.append(now - 1)
            check[now - 1] = True
            dist[now - 1] = dist[now] + 1
    
    if now + 1 < MAX:
        if not check[now + 1]:
            q.append(now + 1)
            check[now + 1] = True
            dist[now + 1] = dist[now] + 1
    
    if now * 2 < MAX:
        if not check[now * 2]:
            q.append(now * 2)
            check[now * 2] = True
            dist[now * 2] = dist[now] + 1
print(dist[k])