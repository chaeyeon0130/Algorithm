import sys

input = sys.stdin.readline

height, width = map(int, input().split())

if height == 1:
    print(1)
elif height == 2:
    print(min(4, (width + 1) // 2))
elif height >= 3:
    if width >= 7:
        print(width - 2)
    else:
        print(min(4, width))