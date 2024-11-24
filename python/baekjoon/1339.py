import sys

input = sys.stdin.readline

n = int(input())
words = [list(input().strip()) for _ in range(n)]
alpha_dict = {}
num_lst = []

for word in words:
    for i in range(len(word)):
        if word[i] in alpha_dict:
            alpha_dict[word[i]] += 10 ** (len(word) - i - 1)
        else:
            alpha_dict[word[i]] = 10 ** (len(word) - i - 1)

for val in alpha_dict.values():
    num_lst.append(val)

num_lst.sort(reverse = True)

result = 0
num = 9
for i in num_lst:
    result += num * i
    num -= 1
print(result)