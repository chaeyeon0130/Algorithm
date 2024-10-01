# import sys

# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     a = [[] for _ in range(n)]
#     color = [0] * n
    
#     for _ in range(m):
#         u, v = map(int, input().split())
#         a[u - 1].append(v - 1)
#         a[v - 1].append(u - 1)
    
#     def dfs(x, c):
#         color[x] = c
#         for y in a[x]:
#             if color[y] == 0:
#                 dfs(y, 3 - c)
    
#     ans = True
#     for i in range(n):
#         if color[i] == 0:
#             dfs(i, 1)
#     for i in range(n):
#         for j in a[i]:
#             if color[i] == color[j]:
#                 ans = False
    
#     print('YES' if ans else 'NO')
    
import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [[] for _ in range(n)]
    color = [0] * n
    
    for _ in range(m):
        u, v = map(int, input().split())
        a[u - 1].append(v - 1)
        a[v - 1].append(u - 1)
        
    def dfs(x, c):
        color[x] = c
        for y in a[x]:
            if color[y] == 0:
                if not dfs(y, 3 - c):
                    return False
            elif color[y] == color[x]:
                return False
        return True
    
    ans = True
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                ans = False
                break
    
    print('YES' if ans else 'NO')