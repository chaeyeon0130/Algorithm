import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
d = [[-1] * (m + 1) for _ in range(n + 1)]

# 방법1
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         d[i][j] = max(d[i - 1][j], d[i][j - 1]) + arr[i][j]
# print(d[n][m])

# 방법2
# d[1][1] = arr[1][1]
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if j + 1 <= m and d[i][j + 1] < d[i][j] + arr[i][j + 1]:
#             d[i][j + 1] = d[i][j] + arr[i][j + 1]
#         if i + 1 <= n and d[i + 1][j] < d[i][j] + arr[i + 1][j]:
#             d[i + 1][j] = d[i][j] + arr[i + 1][j]
# print(d[n][m])

# 방법3
# def go(i, j):
#     if i < 1 or j < 1:
#         return 0
#     if d[i][j] >= 0:
#         return d[i][j]
#     d[i][j] = max(go(i - 1, j), go(i, j - 1)) + arr[i][j]
#     return d[i][j]
#
# print(go(n, m))

# 방법4
def go(i, j):
    if i > n or j > m:
        return 0
    if d[i][j] >= 0:
        return d[i][j]
    d[i][j] = max(go(i + 1, j), go(i, j + 1)) + arr[i][j]
    return d[i][j]
print(go(1, 1))