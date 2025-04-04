n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

filtered = [i for i in str if i[:len(t)] == t]
filtered.sort()


print(filtered[k-1])