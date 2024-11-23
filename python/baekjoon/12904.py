import sys

input = sys.stdin.readline
s = input().strip()
t = list(input().strip())

while len(t) > len(s):
    word = t[-1]

    if word == 'A':
        t.pop()
    elif word == 'B':
        t.pop()
        t.reverse()

if s == ''.join(t):
    print(1)
else:
    print(0)