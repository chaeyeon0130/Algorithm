import sys

input = sys.stdin.readline

n = int(input())
a = [[0] * 3 for _ in range(n + 1)]
d = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    a[i] = list(map(int, input().split()))

ans = 1000 * 1000 + 1
for k in range(3):
    for i in range(3):
        if i == k:
            d[1][i] = a[1][i]
        else:
            d[1][i] = 1001
    
    for i in range(2, n + 1):
        d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i][0]
        d[i][1] = min(d[i - 1][0], d[i - 1][2]) + a[i][1]
        d[i][2] = min(d[i - 1][0], d[i - 1][1]) + a[i][2]
        
    for i in range(3):
        if i == k:
            continue
        else:
            ans = min(ans, d[n][i])

print(ans)
        
    
             