import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

def dfs(depth, sum):
    global result
    if depth == n:
        if sum == s:
            result += 1
        return

    dfs(depth + 1, sum + arr[depth])
    dfs(depth + 1, sum)

dfs(0, 0)
if s == 0:
    print(result - 1)
else:
    print(result)