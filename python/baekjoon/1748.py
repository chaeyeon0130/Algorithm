import sys

input = sys.stdin.readline

n = int(input())

if n <= 9:
    print(n)
    exit(0)

i = 1
res = 0
while 10 ** i <= n:
    res += ((10 ** i) - (10 ** (i - 1))) * i
    i += 1
if n >= 10 ** (i - 1):
    res += ((n - 10 ** (i - 1)) + 1) * i
print(res)