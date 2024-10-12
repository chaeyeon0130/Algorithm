import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
d = [[-1] * (n + 1) for _ in range(n + 1)]

q = deque()
q.append((1, 0))
d[1][0] = 0
while q:
    s, c = q.popleft()
    
    # 클립보드에 복사
    if d[s][s] == -1:
        d[s][s] = d[s][c] + 1
        q.append((s, s))
        
    # 화면에 붙여넣기
    if s + c <= n and d[s + c][c] == -1:
        d[s + c][c] = d[s][c] + 1
        q.append((s + c, c))
        
    # 화면에서 하나 삭제
    if s - 1 >= 0 and d[s - 1][c] == -1:
        d[s - 1][c] = d[s][c] + 1
        q.append((s - 1, c))
    
# 화면에 S개를 만드는데 걸리는 시간의 최솟값
ans = -1
for i in range(0, n + 1):
    if d[n][i] != -1:
        if ans == -1 or ans > d[n][i]:
            ans = d[n][i]
print(ans)