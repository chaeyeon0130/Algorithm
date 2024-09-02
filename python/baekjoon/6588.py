import sys

input = sys.stdin.readline

a = [False] * 1000001
a[0] = a[1] = True
prime = []
m = int(1000001 ** 0.5) + 1
for i in range(2, m):
    if a[i] == False:
        prime.append(i)
    j = i * 2
    while j <= 1000000:
        if a[j] == False:
            a[j] = True
        j += i
        
while True:
    n = int(input())
    if n == 0:
        exit(0)
    for p in prime:
        if a[n - p] == False:
            print(f"{n} = {p} + {n - p}")
            break