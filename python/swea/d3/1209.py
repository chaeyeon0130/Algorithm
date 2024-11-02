T = 10

for test_case in range(1, T + 1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr_t = list(zip(*arr)) # 전치 행렬
    
    max = 0
    
    # 각 행의 합
    for i in range(100):
        row_sum = sum(arr[i])
        if (max < row_sum):
            max = row_sum
    
    # 각 열의 합
    for i in range(100):
        col_sum = sum(arr_t[i])
        if (max < col_sum):
            max = col_sum
    
    # 좌측 대각선의 합
    left_diagonal_sum = 0
    for i in range(100):
        left_diagonal_sum += arr[i][i]
    if (max < left_diagonal_sum):
        max = left_diagonal_sum
        
    # 우측 대각선의 합
    right_diagonal_sum = 0
    for i in range(100):
        right_diagonal_sum += arr[i][99 - i]
    if (max < right_diagonal_sum):
        max = right_diagonal_sum
        
    print(f'#{test_case} {max}')