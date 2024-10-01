import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in rsange(n)]

for _ in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

check = [False] * n
def dfs(node):
    check[node] = True
    for i in a[node]:
        if check[i] == False:
            dfs(i)

component = 0
for i in range(n):
    if check[i] == False:
        component += 1
        dfs(i)
        
print(component)