import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
if m > 0:
    a = list(map(int, input().split()))
else:
    a = []

broken = [0] * 10
for i in a:
    broken[i] = 1

def possible(c):
    if c == 0:
        return not broken[0]
    len = 0
    while c > 0:
        if broken[c % 10]:
            return 0
        len += 1
        c //= 10
    return len

ans = abs(n - 100)
for c in range(1000001):
    len = possible(c)
    if len:
        ans = min(ans, abs(n - c) + len)
print(ans)