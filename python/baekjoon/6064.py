import sys

input = sys.stdin.readline

t = int(input())

while t > 0:
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    valid = False
    for k in range(x, m * n, m):
        if k % n == y:
            valid = True
            print(k + 1)
            break
    if not valid:
        print(-1)
    
    t -= 1