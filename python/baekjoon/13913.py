import sys
from collections import deque
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
q = deque()

MAX = 200000
n, k = map(int, input().split())
check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)
route = [-1] * (MAX + 1)

check[n] = True
dist[n] = 0
q.append(n)
while q:
    now = q.popleft()
    
    if now - 1 >= 0:
        if not check[now - 1]:
            q.append(now - 1)
            check[now - 1] = True
            route[now - 1] = now
            dist[now - 1] = dist[now] + 1
    
    if now + 1 < MAX:
        if not check[now + 1]:
            q.append(now + 1)
            check[now + 1] = True
            route[now + 1] = now
            dist[now + 1] = dist[now] + 1
    
    if now * 2 < MAX:
        if not check[now * 2]:
            q.append(now * 2)
            check[now * 2] = True
            route[now * 2] = now
            dist[now * 2] = dist[now] + 1

def route_print(n, m):
    if n != m:
        route_print(n, route[m])
    print(m, end = ' ')

# ans = []
# value = k
# ans.append(value)
# while True:
#     value = route[value]
#     if n == value:
#         break
#     ans.append(value)
# ans.append(n)
# while ans:
#     print(ans.pop(), end = ' ')

print(dist[k])
route_print(n, k)