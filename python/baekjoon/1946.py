import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr = sorted(arr)

    second_ranking = arr[0][1]
    count = 0
    for i in range(n):
        if second_ranking >= arr[i][1]:
            count += 1
            second_ranking = arr[i][1]
    print(count)