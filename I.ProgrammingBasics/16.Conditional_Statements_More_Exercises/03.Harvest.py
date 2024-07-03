from math import floor
from math import ceil

square_meters_vineyard = int(input())
grape_for_square_meter = float(input())
liters_wine_needed = int(input())
workers_count = int(input())

total_grape_kg = square_meters_vineyard * grape_for_square_meter
grape_for_wine = total_grape_kg * 0.4
liters_wine_produced = grape_for_wine / 2.5

if liters_wine_produced < liters_wine_needed:
    insufficient_wine = liters_wine_needed - liters_wine_produced
    print(f'It will be a tough winter! More {floor(insufficient_wine)} liters wine needed.')
else:
    wine_left = liters_wine_produced - liters_wine_needed
    wine_for_1_worker = wine_left / workers_count
    print(f'Good harvest this year! Total wine: {floor(liters_wine_produced)} liters.')
    print(f'{ceil(wine_left)} liters left -> {ceil(wine_for_1_worker)} liters per person.')