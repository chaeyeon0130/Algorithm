import sys

input = sys.stdin.readline

n = int(input())
a = [list(input().strip()) for _ in range(n)]
result = 0

def check_row(row):
    max_list = []
    max_count = 1
    comp = a[row][0]
    for i in range(1, n):
        if comp == a[row][i]:
            max_count += 1
        else:
            max_list.append(max_count)
            max_count = 1
            comp = a[row][i]
    max_list.append(max_count)
    return max(max_list)

def check_col(col):
    max_list = []
    max_count = 1
    comp = a[0][col]
    for i in range(1, n):
        if comp == a[i][col]:
            max_count += 1
        else:
            max_list.append(max_count)
            max_count = 1
            comp = a[i][col]
    max_list.append(max_count)
    return max(max_list)

for i in range(n):
    result = max(result, check_row(i))

for i in range(n):
    result = max(result, check_col(i))

for i in range(n):
    for j in range(1, n):
        a[i][j - 1], a[i][j] = a[i][j], a[i][j - 1]
        result = max(result, check_row(i), check_col(j), check_col(j -1))
        a[i][j - 1], a[i][j] = a[i][j], a[i][j - 1]

for i in range(n):
    for j in range(1, n):
        a[j - 1][i], a[j][i] = a[j][i], a[j - 1][i]
        result = max(result, check_col(i), check_row(j), check_row(j - 1))
        a[j - 1][i], a[j][i] = a[j][i], a[j - 1][i]
print(result)