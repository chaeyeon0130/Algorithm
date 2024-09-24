import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

LIS = [1] * n
RLIS = [1] * n
LBS = [0] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i] and LIS[j] + 1 > LIS[i]:
            LIS[i] = LIS[j] + 1

for i in reversed(range(n)):
    for j in range(i + 1, n):
        if a[j] < a[i] and RLIS[j] + 1 > RLIS[i]:
            RLIS[i] = RLIS[j] + 1

for i in range(n):
    LBS[i] = LIS[i] + RLIS[i] - 1

print(max(LBS))