import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0] * 2] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j - 1]
        if arr[j][0] <= i:
            dp[i][j] = max(dp[i][j], dp[i - arr[j][0]][j - 1] + arr[j][1])
print(dp[k][n])