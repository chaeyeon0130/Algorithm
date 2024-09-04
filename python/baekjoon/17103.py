import sys

max = 1000000
e = [True] * (max + 1)
e[0] = e[1] = False
prime = []
for i in range(2, max + 1):
    if e[i] == True:
        prime.append(i)
        j = i * 2
        while j <= max:
            e[j] = False
            j += i
    
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    for p in prime:
        if p > n - p:
            break
        if e[n - p] == True:
            result += 1
    print(result)