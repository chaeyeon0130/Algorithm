import sys

input = sys.stdin.readline

# 인덱스는 카드 개수를 의미함
d = [0] * 1001

n = int(input())
p = list(map(int, input().split()))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + p[j - 1])
print(d[n])