import sys
from itertools import combinations

input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]
# combi = list(combinations(arr, 7))
# for i in combi:
#     if sum(i) == 100:
#         i = list(i)
#         i.sort()
#         for j in i:
#             print(j)
#         break

ans_list = []
def combi(n, ans, r):
    if n == len(arr):
        if len(ans) == r:
            temp = [i for i in ans]
            ans_list.append(temp)
        return
    ans.append(arr[n])
    combi(n + 1, ans, r)
    ans.pop()
    combi(n + 1, ans, r)
combi(0, [], 7)
for i in ans_list:
    if sum(i) == 100:
        i.sort()
        for j in i:
            print(j)
        break