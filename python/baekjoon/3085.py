import sys

input = sys.stdin.readline
n = int(input())
a = [list(input().strip()) for _ in range(n)]

ans = 0
def check_row(c):
    compar = a[c][0]
    count = 1
    global ans
    for i in range(1, n):
        if compar == a[c][i]:
            count += 1
        else:
            ans = max(ans, count)
            compar = a[c][i]
            count = 1
    ans = max(ans, count)
            
def check_col(c):
    compar = a[0][c]
    count = 1
    global ans
    for i in range(1, n):
        if compar == a[i][c]:
            count += 1
        else:
            ans = max(ans, count)
            compar = a[i][c]
            count = 1
    ans = max(ans, count)
    
for i in range(n):
    check_row(i)
    
for i in range(n):
    check_col(i)
    
for i in range(n): # 행
    for j in range(n): # 열
        # 오른쪽 -> 마지막 열이 아닐 때만
        if j != n - 1:
            if a[i][j] != a[i][j + 1]:
                a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
                check_row(i)
                check_col(j)
                check_col(j + 1)
                a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
        # 아래쪽 -> 마지막 행이 아닐 때만
        if i != n - 1:
            if a[i][j] != a[i + 1][j]:
                a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
                check_row(i)
                check_row(i + 1)
                check_col(j)
                a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]

print(ans)