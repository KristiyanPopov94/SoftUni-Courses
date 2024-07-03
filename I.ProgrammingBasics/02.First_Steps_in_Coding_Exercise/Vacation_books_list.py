pagesCount = int(input())
pagesAnHour = int(input())
daysCount = int(input())

hoursNeeded = pagesCount / pagesAnHour
hoursEveryDay = hoursNeeded / daysCount

print(round(hoursEveryDay))