import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = -1
                queue.append((nx, ny))
    return count

index = 0
count = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            index += 1
            arr[i][j] = -1
            queue.append((i, j))
            index_count = bfs()
            count.append(index_count)

print(index)
count.sort()
print(*count, sep = '\n')