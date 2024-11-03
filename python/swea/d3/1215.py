T = 10

for test_case in range(1, T + 1):
    size = int(input())
    board = [list(input()) for _ in range(8)]
    
    count = 0
    # 행
    for i in range(0, 8):
        for j in range(0, 8 - size + 1):
            mid = size // 2
            if size % 2 == 0:
                if (board[i][j:j + mid]) == list(reversed(board[i][j + mid:j + size])):
                    count += 1
            else:
                if (board[i][j:j + mid + 1]) == list(reversed(board[i][j + mid:j + size])):
                    count += 1
    
    # 열
    for i in range(0, 8):
        for j in range(0, 8 - size + 1):
            mid = size // 2
            if size % 2 == 0:
                if [row[i] for row in board[j:j + mid]] == list(reversed([row[i] for row in board[j + mid:j + size]])):
                    count += 1
            else:
                if [row[i] for row in board[j:j + mid + 1]] == list(reversed([row[i] for row in board[j + mid:j + size]])):
                    count += 1
    
    print(f'#{test_case} {count}')