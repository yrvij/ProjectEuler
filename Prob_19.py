# Problem 19: Counting Sundays -

normal_year = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

leap_year = {
    1 : 31,
    2 : 29,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

def check_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0
    
start = 1901
sundays = 0
day = 2 # January 1, 1901 was a Tuesday 

while start <= 2000:
    if check_leap_year(start):
        for i in range(1,13):
            if leap_year[i] == 31:
                day += 3
                day %= 7
                if day == 0:
                    sundays += 1
            elif leap_year[i] == 30:
                day += 2
                day %= 7
                if day == 0:
                    sundays += 1
            else:
                day += 1
                day %= 7
                if day == 0:
                    sundays += 1
                    
    else:
        for i in range(1,13):
            if normal_year[i] == 31:
                day += 3
                day %= 7
                if day == 0:
                    sundays += 1
            elif normal_year[i] == 30:
                day += 2
                day %= 7
                if day == 0:
                    sundays += 1    
            else:
                day %= 7
                if day == 0:
                    sundays += 1
                            
    start += 1

print(sundays)   
