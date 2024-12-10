import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    dist[start] = 0

    hq = []
    heapq.heappush(hq, [dist[start], start])
    while hq:
        u_dis, u = heapq.heappop(hq)

        if u_dis > dist[u]:
            continue

        for v in graph[u]:
            if v[0] + dist[u] < dist[v[1]]:
                dist[v[1]] = v[0] + dist[u]
                heapq.heappush(hq, [dist[v[1]], v[1]])

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
INF = 100000 * 1000 + 1
dist = [INF] * (n + 1)

for _ in range(m):
    v1, v2, c = map(int, input().split())
    graph[v1].append((c, v2))

start, end = map(int, input().split())

dijkstra(start)

print(dist[end])

