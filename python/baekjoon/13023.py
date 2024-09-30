import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = [] # 간선리스트
matrix = [[False] * n for _ in range(n)] # 인접행렬
list = [[] for _ in range(n)] # 인접리스트
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))
    edges.append((b, a))
    matrix[a][b] = matrix[b][a] = True
    list[a].append(b)
    list[b].append(a)

m *= 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not matrix[B][C]:
            continue
        for E in list[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            exit(0)
print(0)