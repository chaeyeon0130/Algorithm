T = 10

for test_case in range(1, T + 1):
    n = int(input())
    heights = list(map(int, input().split()))

    result = 0
    for i in range(2, n - 2):
        if (heights[i] == 0):
            continue
        
        max_height = max(heights[i - 2], heights[i - 1], heights[i + 1], heights[i + 2])
        
        if (heights[i] > max_height):
            result += heights[i] - max_height
    
    print("#%d %d" %(test_case, result))