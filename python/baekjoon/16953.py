import sys

input = sys.stdin.readline

a, b = map(int, input().split())
result = 1
while b > a:
    if b % 2 == 0:
        b = b // 2
    elif b % 10 == 1:
        b = b // 10
    else:
        break
    result += 1

if b == a:
    print(result)
else:
    print(-1)