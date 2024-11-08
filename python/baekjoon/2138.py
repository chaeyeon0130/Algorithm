import sys

input = sys.stdin.readline
n = int(input())
a1 = list(map(int, list(input().strip())))
a2 = a1[:]
goal = list(map(int, list(input().strip())))

def change(arr, i):
    for j in range(i - 1, i + 2):
        if 0 <= j < n:
            arr[j] = 1 - arr[j]
    
# 0번 전구를 누른 경우
change(a1, 0)
a1_count = 1
a1_changeable = False
for i in range(0, n - 1):
    if a1[i] != goal[i]:
        a1_count += 1
        change(a1, i + 1)
        
if a1[n - 1] == goal[n - 1]:
    a1_changeable = True
         
# 0번 전구를 누르지 않은 경우
a2_count = 0
a2_changeable = False
for i in range(0, n - 1):
    if a2[i] != goal[i]:
        a2_count += 1
        change(a2, i + 1)

if a2[n - 1] == goal[n - 1]:
    a2_changeable = True

# 정답 산출
if a1_changeable and a2_changeable:
    print(min(a1_count, a2_count))
elif a1_changeable:
    print(a1_count)
elif a2_changeable:
    print(a2_count)
else:
    print(-1)