import sys

n = int(input())
result = []

if n == 0:
    result.append(0)
while n != 0:
    if n % -2 != 0:
        result.append(1)
        n = n // -2 + 1
    else:
        result.append(0)
        n = n // -2
print(''.join(map(str, result[::-1])))
