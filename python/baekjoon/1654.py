import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cables = [int(input().strip()) for _ in range(n)]

def check(length):
    global result
    count = 0
    for cable in cables:
        count += cable // length
    return count >= k

max_length = 0
for cable in cables:
    if cable > max_length:
        max_length = cable

left = 1
right = max_length
result = 0
while left <= right:
    mid = (left + right) // 2

    if check(mid):
        if result < mid:
            result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)