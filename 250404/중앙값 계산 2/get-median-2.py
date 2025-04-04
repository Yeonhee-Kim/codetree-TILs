N = int(input())
str = list(map(int, input().split()))

for i in range(len(str)):
    if i % 2 != 0:
        continue
    sort_str = sorted(str[:i+1])
    print(sort_str[i // 2], end=" ")