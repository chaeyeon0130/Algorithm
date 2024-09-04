import sys

def ten_to_B(n, b):
    if n <= 0:
        return
    ten_to_B(n // b, b)
    print(n % b, end = ' ')

input = sys.stdin.readline
a, b = map(int, input().split())
m = int(input())
e = list(map(int, input().split()))
ten = 0
for i in e:
    ten = ten * a + i
ten_to_B(ten, b)