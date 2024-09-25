import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = [0] * n
rd = [0] * n
# 연속합 구하기(앞에서부터)
d[0] = a[0]
for i in range(1, n):
    d[i] = max(a[i], d[i - 1] + a[i])

# 연속합 구하기(뒤에서부터)
rd[n - 1] = a[n - 1]
for i in range(n - 2, -1, -1):
    rd[i] = max(a[i], rd[i + 1] + a[i])

# i를 제외한 연속합 구하기
ans = max(d)
for i in range(1, n - 1):
    ans = max(ans, d[i - 1] + rd[i + 1])
        
print(ans)