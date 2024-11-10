import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [0] * 3

def check(x, y, n):
    first = arr[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n) :
            if arr[i][j] != first:
                return False
    
    return True

def divide(x, y, n):
    if check(x, y, n):
        ans[arr[x][y] + 1] += 1
        return
    
    size = n // 3
    for i in range(0, 3):
        for j in range(0, 3):
            divide(x + i * size, y + j * size, size)

divide(0, 0, n)
for i in range(0, 3):
    print(ans[i])
    