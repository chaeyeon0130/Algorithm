from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    s = int(input())
    s_list = deque(input().split())

    while s_list:
        if s_list.popleft() == "I":
            index = int(s_list.popleft())
            count = int(s_list.popleft())

            for _ in range(count):
                if index < len(arr):
                    arr.insert(index, int(s_list.popleft()))
                else:
                    arr.append(int(s_list.popleft()))
                index += 1

    print(f"#{test_case} ", end = '')
    print(*arr[:10])