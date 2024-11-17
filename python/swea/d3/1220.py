T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    deadlock = 0
    for j in range(0, n): # 열
        last = 2
        for i in range(0, n): # 행
            if last == 1 and arr[i][j] == 2:
                deadlock += 1
            if arr[i][j] != 0:
                last = arr[i][j]

    print(f'#{test_case} {deadlock}')