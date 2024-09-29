import sys

input = sys.stdin.readline

n = int(input())
len = len(str(n))

ans = 0
for i in range(1, len + 1):
    if i == len:
        num = n - 10 ** (len - 1) + 1
        ans += num * len
    else:
        num = 10 ** i - 10 ** (i - 1)
        ans += num * i
        
print(ans)
