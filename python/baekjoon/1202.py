import sys
import heapq

n, k = map(int, input().split())
arr = []
max_heap = []
max_value = 1000000

for _ in range(n):
    arr.append(list(map(int, input().split())))

for _ in range(k):
    arr.append([int(input()), max_value + 1])

arr.sort() # 보석, 가방 무게를 기준으로 오름차순 정렬

result = 0
for a in arr:
    if a[1] != max_value + 1: # 보석
        heapq.heappush(max_heap, (-a[1], a[1]))
    else: # 가방
        if max_heap:
            result += heapq.heappop(max_heap)[1]
print(result)