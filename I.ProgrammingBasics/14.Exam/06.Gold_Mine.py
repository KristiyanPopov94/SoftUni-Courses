locations_count = int(input())

target_average_gold_a_day = 0
target_days = 0

gold_mined = 0
days_mined = 0
average_gold_mined_day = 0

target_achieved = False
for _ in range(locations_count):
    target_average_gold_a_day = float(input())
    target_days = int(input())

    for _ in range(target_days):
        gold_mined += float(input())
        average_gold_mined_day = gold_mined / target_days
        days_mined += 1

        if average_gold_mined_day >= target_average_gold_a_day:
            target_achieved = True

    if target_achieved:
        print(f'Good job! Average gold per day: {average_gold_mined_day:.2f}.')
    else:
        gold_needed = target_average_gold_a_day - average_gold_mined_day
        print(f'You need {gold_needed:.2f} gold.')

    gold_mined = 0
    days_mined = 0
    target_achieved = False
