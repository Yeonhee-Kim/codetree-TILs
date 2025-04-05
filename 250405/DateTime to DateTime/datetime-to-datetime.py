day, hour, min = 11, 11, 11
cnt = 0

a, b, c = map(int, input().split())
if (a < 11) or (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
    print(-1)
else:
    while True:
        if day == a and hour == b and min == c:
            break
    
        cnt += 1
        min += 1
    
        if min == 60:
            hour += 1
            min = 0
    
        if hour == 24:
            day += 1
            hour = 0
    print(cnt)
