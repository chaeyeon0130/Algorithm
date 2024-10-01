# 인접리스트
from collections import deque

n, m, start = map(int, input().split())
a = [[] for _ in range(n + 1)]
check = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1, n + 1):
    a[i].sort()

def dfs(x):
    global check
    check[x] = True
    print(x, end = ' ')
    for y in a[x]:
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()

# 간선리스트
from collections import deque

n, m, start = map(int, input().split())
edges = []
check = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    edges.append((v, u))

m *= 2

edges.sort()

cnt = [0] * (n + 1)

for u, v in edges:
    cnt[u] += 1
    
for i in range(1, n + 1):
    cnt[i] += cnt[i - 1]

def dfs(x):
    global check
    check[x] = True
    print(x, end = ' ')
    for i in range(cnt[x - 1], cnt[x]):
        y = edges[i][1]
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for i in range(cnt[x - 1], cnt[x]):
            y = edges[i][1]
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()

# 비재귀 구현소스 - 1
from collections import deque

n, m, start = map(int, input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

for i in range(1, n + 1):
    a[i].sort()

def dfs(node):
    check = [False] * (n + 1)
    stack = []
    stack.append((node, 0))
    check[node] = True
    print(node, end = ' ')
    while stack:
        x, start = stack.pop()
        for i in range(start, len(a[x])):
            y = a[x][i]
            if check[y] == False:
                print(y, end = ' ')
                check[y] = True
                stack.append((x, i + 1))
                stack.append((y, 0))
                break

def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)
                
dfs(start)
print()
bfs(start)
print()

# 비재귀 구현소스 - 2
from collections import deque
def dfs(n, a, node):
    check = [False] * (n + 1)
    start = [0] * (n + 1)
    stack = []
    stack.append(node)
    check[node] = True
    print(node, end = ' ')
    while stack:
        node = stack.pop()
        while start[node] < len(a[node]):
            nxt = a[node][start[node]]
            if check[nxt] == False:
                print(nxt, end = ' ')
                check[nxt] = True
                stack.append(node)
                stack.append(nxt)
                break
            start[node] += 1
            
def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)
    
n, m, start = map(int, input().split())
a = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1, n + 1):
    a[i].sort()
dfs(n, a, start)
print()
bfs(start)
print()