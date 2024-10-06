import sys

input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(n)]
check = [False] * n
order = [-1] * n

for _ in range(n - 1):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

d = list(map(lambda x: int(x) - 1, input().split()))

for i in range(n):
    order[d[i]] = i

# a 인접리스트를 order 배열을 반영해서 정렬
for i in range(n):
    a[i].sort(key = lambda x: order[x])


dfs_order = []
def dfs(x):
    if check[x]:
        return
    check[x] = True
    dfs_order.append(x)
    for y in a[x]:
        if not check[y]:
            dfs(y)
            
dfs(0)

for i in range(n):
    if d[i] != dfs_order[i]:
        print(0)
        exit(0)
print(1)