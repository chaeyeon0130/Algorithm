T = 10

for test_case in range(1, T + 1):
    d = int(input())
    heights = list(map(int, input().split()))
    
    for _ in range(d):
        max_value = max(heights)
        min_value = min(heights)
        
        if max_value == 0:
            break
        
        heights[heights.index(max_value)] = max_value - 1
        heights[heights.index(min_value)] = min_value + 1
        
    final_max = max(heights)
    final_min = min(heights)
    result = final_max - final_min
    
    print(f'#{test_case} {result}')