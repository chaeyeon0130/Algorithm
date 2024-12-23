import sys

input = sys.stdin.readline

e, s, m = map(int, input().split())

year = 1
while True:
    if (year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
        break
    year += 1
print(year)

# import sys
#
# input = sys.stdin.readline
# e, s, m = map(int, input().split())
#
# E = 0
# S = 0
# M = 0
# year = 0
# while True:
#     if E == e and S == s and M == m:
#         break
#     E += 1
#     S += 1
#     M += 1
#     year += 1
#
#     if E > 15:
#         E %= 15
#     if S > 28:
#         S %= 28
#     if M > 19:
#         M %= 19
# print(year)