# import sys

# input = sys.stdin.readline
# n, b = input().split()
# b = int(b)

# result = 0
# exp = len(n) - 1
# for c in n:
#     if 'A' <= c <= 'Z':
#         c = ord(c) - ord('A') + 10
#     result += int(c) * (b ** exp)
#     exp -= 1
# print(result)

import sys

input = sys.stdin.readline
s, b = input().split()
b = int(b)
ans = 0
for ch in s:
    if '0' <= ch <= '9':
        ans = ans * b + (ord(ch) - ord('0'))
    else:
        ans = ans * b + (ord(ch) - ord('A') + 10)
print(ans)