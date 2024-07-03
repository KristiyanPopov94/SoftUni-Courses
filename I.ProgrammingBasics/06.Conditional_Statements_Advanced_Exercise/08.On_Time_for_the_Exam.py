exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_total_minutes = exam_hour * 60 + exam_minutes
arrival_total_minutes = arrival_hour * 60 + arrival_minutes

if arrival_total_minutes + 30 < exam_total_minutes:
    if exam_total_minutes - arrival_total_minutes >= 60:
        print('Early')
        print(f'{(exam_total_minutes - arrival_total_minutes) // 60}:'
              f'{((exam_total_minutes - arrival_total_minutes) % 60):02d} hours before the start')
    else:
        print('Early')
        print(f'{(exam_total_minutes - arrival_total_minutes)} minutes before the start')
elif arrival_total_minutes < exam_total_minutes:
    print('On time')
    print(f'{(exam_total_minutes - arrival_total_minutes):} minutes before the start')
elif arrival_total_minutes == exam_total_minutes:
    print('On time')
elif arrival_total_minutes - 60 < exam_total_minutes:
    print('Late')
    print(f'{(arrival_total_minutes - exam_total_minutes):} minutes after the start')
else:
    print('Late')
    print(f'{(arrival_total_minutes - exam_total_minutes) // 60}:'
          f'{((arrival_total_minutes - exam_total_minutes) % 60):02d} hours after the start')
