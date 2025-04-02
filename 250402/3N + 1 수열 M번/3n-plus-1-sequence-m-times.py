T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0

    while N > 1:
        if N == 1:
            break
        if N % 2 == 0:
            N = N // 2
        else:
            N = N * 3 + 1
        cnt = cnt + 1

    print(cnt)