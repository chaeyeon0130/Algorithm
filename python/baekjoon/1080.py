import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [list(map(int, list(input().strip()))) for _ in range(n)]

def flip(c_row, c_col):
    for i in range(c_row - 1, c_row + 2):
        for j in range(c_col - 1, c_col + 2):
            a[i][j] = 1 - a[i][j]

count = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            count += 1
            flip(i + 1, j + 1)

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            count = -1

print(count)