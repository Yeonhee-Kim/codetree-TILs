def sort_number(N, j):
    for i in range(N):
        for _ in range(N):
            print(j, end=" ")
            j += 1
            if j == 10:
                j = 1
        print()

N = int(input())
j = 1
sort_number(N, j)