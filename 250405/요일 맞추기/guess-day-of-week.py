m1, d1, m2, d2 = map(int, input().split())

day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 날짜를 일수로 환산하는 함수
def date_to_days(month, day):
    return sum(day_of_month[:month]) + day

start = date_to_days(m1, d1)
end = date_to_days(m2, d2)
diff = end - start

current = (0 + diff) % 7

print(day[current])