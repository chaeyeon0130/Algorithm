import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [-1] * n

# d[0] = 0
# for i in range(n):
#     for j in range(i):
#         if d[j] != -1 and i - j <= arr[j]:
#             if d[i] == -1 or d[i] > d[j] + 1:
#                 d[i] = d[j] + 1
# print(d[n - 1])

# 방법2
d[0] = 0
for i in range(n):
    if d[i] == -1:
        continue
    for j in range(1, arr[i] + 1):
        if i + j >= n:
            break
        if d[i + j] == -1 or d[i + j] > d[i] + 1:
            d[i + j] = d[i] + 1
print(d[n - 1])