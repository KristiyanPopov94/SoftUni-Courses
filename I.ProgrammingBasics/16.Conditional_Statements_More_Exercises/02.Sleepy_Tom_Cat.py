holidays = int(input())

workdays = 365 - holidays

minutes_workdays = workdays * 63
minutes_holidays = holidays * 127

total_minutes = minutes_holidays + minutes_workdays

if total_minutes <= 30000:
    time_difference = 30000 - total_minutes
    minutes = time_difference % 60
    hours = time_difference // 60
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    time_difference = total_minutes - 30000
    minutes = time_difference % 60
    hours = time_difference // 60
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')