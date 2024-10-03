import sys
from collections import deque
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
n = int(input())
list = [[] for _ in range(n)]
check = [0] * n

for _ in range(n):
    u, v = map(int, input().split())
    list[u - 1].append(v - 1)
    list[v - 1].append(u - 1)

# -2 : 사이클 찾음, 포함되지 않음
# -1 : 사이클 못 찾음
# 0 ~ n - 1 : 사이클 찾음
def dfs(s, ps):
    if check[s]:
        return s
    check[s] = 1
    for i in list[s]:
        if i == ps:
            continue
        result = dfs(i, s)
        if result == -2:
            return -2
        if result >= 0:
            check[s] = 2
            if result == s:
                return - 2
            else:
                return result
    return -1

dfs(0, -1)

d = deque()
dist = [-1] * n

for i in range(n):
    if check[i] == 2:
        dist[i] = 0
        d.append(i)
        
while d:
    c = d.popleft()
    for i in list[c]:
        if dist[i] == -1:
            dist[i] = dist[c] + 1
            d.append(i)

print(*dist)