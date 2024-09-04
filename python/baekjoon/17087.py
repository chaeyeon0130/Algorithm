import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = abs(s - a[i])

result = a[0]
for i in range(1, n):
    result = gcd(result, a[i])
print(result)