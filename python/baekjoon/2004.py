import sys

input = sys.stdin.readline
n, m = map(int, input().split())

def count_0(i, divisor):
    count = 0
    v = divisor
    while i >= divisor:
        count += i // divisor
        divisor *= v
    return count

two = 0
five = 0
two += count_0(n, 2)
two -= count_0(n - m, 2)
two -= count_0(m, 2)
five += count_0(n, 5)
five -= count_0(n - m, 5)
five -= count_0(m, 5)
print(min(two, five))