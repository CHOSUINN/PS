day_of_the_week = {0 : "MON", 1 : "TUE", 2 : "WED", 3 : "THU", 4 : "FRI", 5 : "SAT", 6 : "SUN"}
x, y = map(int,input().split())
days = y
for i in range(1, x) :
    if i < 8 and i % 2 == 1 :
        days += 31
    elif i < 8 and i % 2 == 0 :
        if i == 2 :
            days += 28
        else :
            days += 30
    elif i > 8 and i % 2 == 1 :
        days += 30
    else :
        days += 31
key_val = (days - 1) % 7        # 인덱스는 0부터 시작하는데 반해 일(日)은 1부터 시작하기에 1을 빼주었다.
print(day_of_the_week[key_val])