days_count = int(input())
hours_daily = int(input())

total_sum = 0
total_sum_for_day = 0

for days in range(1, days_count + 1):
    for hours in range(1, hours_daily + 1):
        if days % 2 == 0 and hours % 2 == 1:
            total_sum += 2.50
            total_sum_for_day += 2.50
        elif days % 2 == 1 and hours % 2 == 0:
            total_sum += 1.25
            total_sum_for_day += 1.25
        else:
            total_sum += 1
            total_sum_for_day += 1
    print(f'Day: {days} - {total_sum_for_day:.2f} leva')
    total_sum_for_day = 0

print(f'Total: {total_sum:.2f} leva')