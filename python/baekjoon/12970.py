n, k = map(int, input().split())

result = []
for a in range(1, n):
    b = n - a

    if a * b < k:
        continue

    cnt_lst = [0] * (b + 1)
    for _ in range(a):
        cnt = min(b, k)
        cnt_lst[cnt] += 1
        k -= cnt

    for i in range(b, -1, -1):
        for _ in range(cnt_lst[i]):
            result.append('A')
        if i > 0:
            result.append('B')
    break

if not result:
    print(-1)
else:
    print(''.join(result))