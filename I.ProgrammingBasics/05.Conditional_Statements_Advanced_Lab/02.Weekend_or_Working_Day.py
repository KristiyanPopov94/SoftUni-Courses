day = input()
working_day = False
weekend = False

if day == "Monday":
    working_day = True
elif day == "Tuesday":
    working_day = True
elif day == "Wednesday":
    working_day = True
elif day == "Thursday":
    working_day = True
elif day == "Friday":
    working_day = True
elif day == "Saturday":
    weekend = True
elif day == "Sunday":
    weekend = True

if working_day:
    print('Working day')
elif weekend:
    print('Weekend')
else:
    print('Error')
