import sys

input = sys.stdin.readline

n = int(input())
p = input().strip()

o = [0] * n
for i in range(n):
    o[i] = int(input())

stack = []
for c in p:
    if 'A' <= c <= 'Z':
        stack.append(o[ord(c) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if c == '*':
            stack.append(a * b)
        elif c == '/':
            stack.append(a / b)
        elif c == '+':
            stack.append(a + b)
        elif c == '-':
            stack.append(a - b)

print(f'{stack[-1]:.2f}')