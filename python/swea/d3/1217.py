T = int(input())

def solution(n, m):
    if m == 1:
        return n
    else:
        m -= 1
        return n * solution(n, m)

for _ in range(T):
    test_num = int(input())
    n, m = map(int, input().split())
    print(f"#{test_num} {solution(n, m)}")