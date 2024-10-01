# # bfs
# import sys
# from collections import deque, Counter
# from functools import reduce

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# def bfs(i, j, cnt):
#     q = deque()
#     q.append((i, j))
#     d[i][j] = cnt
#     while q:
#         i, j = q.popleft()
#         for k in range(4):
#             nx, ny = i + dx[k], j + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if a[nx][ny] == 1 and d[nx][ny] == 0:
#                     q.append((nx, ny))
#                     d[nx][ny] = cnt
            
# input = sys.stdin.readline
# n = int(input())
# a = [list(map(int, list(input().strip()))) for _ in range(n)]
# d = [[0] * n for _ in range(n)]
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if a[i][j] == 1 and d[i][j] == 0:
#             cnt += 1
#             bfs(i, j, cnt)

# ans = reduce(lambda x, y : x + y, d)
# ans = [x for x in ans if x > 0]
# ans = sorted(list(Counter(ans).values()))
# print(cnt)
# print('\n'.join(map(str, ans)))

# dfs
import sys
from collections import deque, Counter
from functools import reduce

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(i, j, cnt):
    d[i][j] = cnt
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1 and d[nx][ny] == 0:
                dfs(nx, ny, cnt)
            
input = sys.stdin.readline
n = int(input())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
d = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and d[i][j] == 0:
            cnt += 1
            dfs(i, j, cnt)

ans = reduce(lambda x, y : x + y, d)
ans = [x for x in ans if x > 0]
ans = sorted(list(Counter(ans).values()))
print(cnt)
print('\n'.join(map(str, ans)))