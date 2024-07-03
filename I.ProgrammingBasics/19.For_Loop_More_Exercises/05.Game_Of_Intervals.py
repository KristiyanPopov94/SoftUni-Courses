turns = int(input())

total_points = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for _ in range(0, turns):
    number = int(input())

    if number < 0 or number > 50:
        total_points /= 2
        invalid_numbers += 1
    elif number <= 9:
        total_points += number * 0.20
        from_0_to_9 += 1
    elif number <= 19:
        total_points += number * 0.30
        from_10_to_19 += 1
    elif number <= 29:
        total_points += number * 0.40
        from_20_to_29 += 1
    elif number <= 39:
        total_points += 50
        from_30_to_39 += 1
    elif number <= 50:
        total_points += 100
        from_40_to_50 += 1

from_0_to_9_in_percent = from_0_to_9 / turns * 100
from_10_to_19_in_percent = from_10_to_19 / turns * 100
from_20_to_29_in_percent = from_20_to_29 / turns * 100
from_30_to_39_in_percent = from_30_to_39 / turns * 100
from_40_to_50_in_percent = from_40_to_50 / turns * 100
invalid_numbers_in_percent = invalid_numbers / turns * 100

print(f'{total_points:.2f}')
print(f'From 0 to 9: {from_0_to_9_in_percent:.2f}%')
print(f'From 10 to 19: {from_10_to_19_in_percent:.2f}%')
print(f'From 20 to 29: {from_20_to_29_in_percent:.2f}%')
print(f'From 30 to 39: {from_30_to_39_in_percent:.2f}%')
print(f'From 40 to 50: {from_40_to_50_in_percent:.2f}%')
print(f'Invalid numbers: {invalid_numbers_in_percent:.2f}%')