import sys

input = sys.stdin.readline

x = input().strip()
y = input().strip()

lcs = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
print(lcs[len(x)][len(y)])