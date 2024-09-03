import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    l = input().split()
    n = int(l[0])
    e = list(map(int, l[1:]))
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            result += gcd(e[i], e[j])
    print(result)