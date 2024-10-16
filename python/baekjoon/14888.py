import sys

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1
    
    a[i - 1], a[j] = a[j], a[i - 1]
    
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    
    return True
        
def calc(a, operator):
    result = a[0]
    for i, oper in enumerate(operator):
        if oper == '+':
            result += a[i + 1]
        if oper == '-':
            result -= a[i + 1]
        if oper == '*':
            result *= a[i + 1]
        if oper == '/':
            if result < 0:
                result = -(-result // a[i + 1])
            else:
                result //= a[i + 1]
                
    return result

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
operator_list = ['+', '-', '*', '/']
operator_count = list(map(int, input().split()))
operator = []

for i in range(4):
    for _ in range(operator_count[i]):
        operator.append(operator_list[i])
operator.sort()
        
ans = []
while True:
    result = calc(a, operator)
    ans.append(result)
    if not next_permutation(operator):
        break

ans.sort()
print(ans[-1])
print(ans[0])
            