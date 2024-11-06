import math

def check():
    for i in range(100, 0, -1):
        str_len = i
        for r in range(100):
            for c in range(100 - str_len):
                #가로
                search = board[r][c:c + str_len]
                if search[:str_len//2] == search[math.ceil(str_len/2):][::-1]:
                    return str_len

                #세로
                search = trans_board[r][c:c + str_len]
                if search[:str_len//2] == search[math.ceil(str_len/2):][::-1]:
                    return str_len
    return

T = 10
for test_case in range(1, T + 1):
    test_num =int(input())
    board = [input() for i in range(100)]
    trans_board = [''.join(list(x)) for x in zip(*board)]
    
    ans = check()
    print(f'#{test_num} {ans}')