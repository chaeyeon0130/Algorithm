import sys

input = sys.stdin.readline

def dfs(depth, sum, plus, minus, mul, div):
    if depth == len(a):
        return (sum, sum)

    results = []
    if plus > 0:
        results.append(dfs(depth + 1, sum + a[depth], plus - 1, minus, mul, div))
    if minus > 0:
        results.append(dfs(depth + 1, sum - a[depth], plus, minus - 1, mul, div))
    if mul > 0:
        results.append(dfs(depth + 1, sum * a[depth], plus, minus, mul - 1, div))
    if div > 0:
        if sum >= 0:
            results.append(dfs(depth + 1, sum // a[depth], plus, minus, mul, div - 1))
        else:
            results.append(dfs(depth + 1, -(-sum // a[depth]), plus, minus, mul, div - 1))

    ans = (
        max(result[0] for result in results),
        min(result[1] for result in results)
    )

    return ans

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
ans = dfs(1, a[0], plus, minus, mul, div)
print(ans[0])
print(ans[1])