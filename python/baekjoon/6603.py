# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# while True:
#     arr = list(map(int, input().split()))
#     k = arr[0]
#     S = arr[1:]
#
#     if k == 0:
#         break
#
#     for i in combinations(S, 6):
#         print(*i)
#     print()

def dfs(depth, idx):
    if depth == 6:
        print(*lotto)
        return

    if idx == len(S):
        return

    lotto.append(S[idx])
    dfs(depth + 1, idx + 1)
    lotto.pop()
    dfs(depth, idx + 1)

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    S = arr[1:]

    if k == 0:
        break

    lotto = []
    dfs(0, 0)
    print()