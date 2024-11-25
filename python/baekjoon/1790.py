import sys

def calc_length(n):
    start = 1
    length = 1

    total_length = 0
    while start <= n:
        end = start * 10 - 1
        if end > n:
            end = n

        total_length += (end - start + 1) * length

        start *= 10
        length += 1
    return total_length

input = sys.stdin.readline
n, k = map(int, input().split())

if calc_length(n) < k:
    print(-1)
    exit(0)

left = 1
right = n
result = 0
while left <= right:
    mid = (left + right) // 2
    length = calc_length(mid)

    if length < k:
        left = mid + 1
    else:
        result = mid
        right = mid - 1
result_str = str(result)
result_length = calc_length(result)
print(result_str[len(result_str) - (result_length - k) - 1])