import sys

input = sys.stdin.readline

arr = [1, 5, 10, 50]

n = int(input())

lst = []
s = set()
def dfs(depth, n, idx):
    if depth == n:
        s.add(sum(lst))
        return
    for i in range(idx, 4):
        lst.append(arr[i])
        dfs(depth + 1, n, i)
        lst.pop()
dfs(0, n, 0)
print(len(s))

