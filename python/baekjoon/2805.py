import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def check(mid):
    height = 0
    for tree in trees:
        if tree >= mid:
            height += tree - mid
    return height >= m

left = 0
right = max(trees)
result = 0
while left <= right:
    mid = (left + right) // 2

    if check(mid):
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1
print(result)