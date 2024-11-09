import sys

input = sys.stdin.readline
n = int(input())
arr = [list(input().strip()) for _ in range(n)]

def flip(current):
    if current == 'H':
        return 'T'
    else:
        return 'H'
    
ans = n * n
for case in range(1 << n):
    total_t_count = 0
    for j in range(n):
        t_count = 0
        for i in range(n):
            current = arr[i][j]
            if (case & (1 << i)) != 0:
                current = flip(current)
            if current == 'T':
                t_count += 1
        total_t_count += min(t_count, n - t_count)
    if ans > total_t_count:
        ans = total_t_count
print(ans)
        