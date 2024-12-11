import sys

input = sys.stdin.readline

# 이산탐색할 값 : 배정된 예산들 중 최댓값인 정수
def go(mid):
    sum = 0
    for i in range(n):
        if arr[i] > mid:
            sum += mid
        else:
            sum += arr[i]
    return sum <= m

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

left = 1
right = max(arr)
result = 0
while left <= right:
    mid = (left + right) // 2
    if go(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)



