import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
if m:
    broken = input().split()
else:
    broken = []

ans = abs(100 - n)
for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - n))
print(ans)