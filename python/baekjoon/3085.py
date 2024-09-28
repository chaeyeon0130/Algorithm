import sys

input = sys.stdin.readline
n = int(input())
a = [list(input().strip()) for _ in range(n)]

def check_row(r):
    max_count = 1
    count = 1
    for i in range(1, n):
        if a[r][i] == a[r][i - 1]:
            count += 1
        else:
            count = 1
        if max_count < count:
            max_count = count
    return max_count
            
def check_col(c):
    max_count = 1
    count = 1
    for i in range(1, n):
        if a[i][c] == a[i - 1][c]:
            count += 1
        else:
            count = 1
        if max_count < count:
            max_count = count
    return max_count
    
for i in range(n):
    check_row(i)
    
for i in range(n):
    check_col(i)

ans = 0
for i in range(n):
    for j in range(n):
        if j != n - 1:
            if a[i][j] != a[i][j + 1]:
                a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
                ans = max(ans, check_row(i))
                ans = max(ans, check_col(j))
                ans = max(ans, check_col(j + 1))
                a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
        if i != n - 1:
            if a[i][j] != a[i + 1][j]:
                a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
                ans = max(ans, check_row(i))
                ans = max(ans, check_row(i + 1))
                ans = max(ans, check_col(j))
                a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]

print(ans)