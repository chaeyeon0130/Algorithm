import sys

input = sys.stdin.readline
n, b = map(int, input().split())
b = int(b)

result = []
while n != 0:
    r = n % b
    if r > 9:
        r = chr(r - 10 + ord('A'))
    n = n // b
    result.append(str(r))
print(''.join(result[::-1]))