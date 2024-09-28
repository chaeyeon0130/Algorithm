# import sys

# input = sys.stdin.readline

# e, s, m = map(int, input().split())

# i = 0
# j = 0
# k = 0
# year = 0
# while True:
#     i += 1
#     j += 1
#     k += 1
#     year += 1
    
#     if i == 16:
#         i = 1
#     if j == 29:
#         j = 1
#     if k == 20:
#         k = 1
    
#     if i == e and j == s and k == m:
#         print(year)
#         exit(0)

import sys

input = sys.stdin.readline

e, s, m = map(int, input().split())

e -= 1
s -= 1
m -= 1

year = 0
while True:
    if year % 15 == e and year % 28 == s and year % 19 == m:
        print(year + 1)
        exit(0)
    year += 1