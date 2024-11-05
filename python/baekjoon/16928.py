import sys
from collections import deque

input = sys.stdin.readline
q = deque()

n, m = map(int, input().split())
dist = [-1] * 101
next = [i for i in range(0, 101)]
for _ in range(n):
    x, y = map(int, input().split())
    next[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    next[u] = v

dist[1] = 0
q.append(1)
while q:
    current_node = q.popleft()
    for i in range(1, 7):
        next_node = current_node + i
        if next_node > 100:
            continue
        
        next_node = next[next_node]
        if (dist[next_node] == -1):
            dist[next_node] = dist[current_node] + 1
            q.append(next_node)

print(dist[100])