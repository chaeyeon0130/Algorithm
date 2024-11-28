import sys

input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input().strip()) for _ in range(n)]
arr.sort()

def check(mid):
    last = arr[0]
    count = 1
    for i in arr:
        if i - last >= mid:
            count += 1
            last = i
    return count >= c

left = 1
right = arr[n - 1] - arr[0]
result = 1
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        if result < mid:
            result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)