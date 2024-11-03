T = int(input())

for test_case in range(1, T + 1):
    t = int(input())
    str = input()
    sentence = input()
    
    count = sentence.count(str)
    
    print(f'#{test_case} {count}')