# import sys

# input = sys.stdin.readline

# a = [int(input()) for _ in range(9)]

# for i in range(9):
#     for j in range(9):
#         if i == j:
#             continue
#         sum = 0
#         for k in range(9):
#             if k != i and k != j:
#                 sum += a[k]
#         if sum == 100:
#             result = [a[k] for k in range(9) if k != i and k != j]
#             result.sort()
#             for num in result:
#                 print(num)
#             exit(0)
            
import sys

a = [int(input()) for _ in range(9)]
a.sort()
total = sum(a)
for i in range(0, 9):
    for j in range(i + 1, 9):
        if total - a[i] - a[j] == 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                print(a[k])
            exit(0)