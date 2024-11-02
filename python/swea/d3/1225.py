from collections import deque

T = 2

for test_case in range(1, T + 1):
    t = int(input())
    arr = list(map(int, input().split()))
    queue = deque(arr)
    
    stop = False
    while (True):
        if stop:
            break
        
        for i in range(1, 6):
            front = queue.popleft()
            back = front - i
            if (back <= 0):
                queue.append(0)
                stop = True
                break
            queue.append(back)
            
    print(f'#{test_case}', *queue)