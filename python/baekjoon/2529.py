import sys
from itertools import permutations

input = sys.stdin.readline

def check(perm):
    for i in range(len(arr)):
        if arr[i] == '<' and perm[i] > perm[i + 1]:
            return False
        if arr[i] == '>' and perm[i] < perm[i + 1]:
            return False
    return True

k = int(input())
arr = input().split()
small = [i for i in range(k + 1)]
big = [9 - i for i in range(k + 1)]

big_perm = permutations(big, k + 1)
for i in big_perm:
    if check(i):
        print(''.join(map(str, i)))
        break

small_perm = list(permutations(small, k + 1))
for i in small_perm:
    if check(i):
        print(''.join(map(str, i)))
        break