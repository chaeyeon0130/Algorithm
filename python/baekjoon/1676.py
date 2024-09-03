# import sys

# n = int(input())

# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i

# factorial_list = list(map(int, str(factorial)))
# count = 0
# for j in range(len(factorial_list) - 1, -1, -1):
#     if factorial_list[j] == 0:
#         count += 1
#     else:
#         break

# print(count)

import sys

n = int(input())

print(n // 5 + n // 25 + n // 125)