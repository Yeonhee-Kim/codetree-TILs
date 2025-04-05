a, b, c, d = map(int, input().split())
day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 0

while True:
    if a == c and b == d:
        break
    
    cnt += 1
    b += 1
    
    if b > day_of_month[a]:
        a += 1
        b = 1

print(cnt+1)