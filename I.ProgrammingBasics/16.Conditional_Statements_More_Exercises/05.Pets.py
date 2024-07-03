from math import floor
from math import ceil

days = int(input())
total_food_kg = int(input())
dog_food_daily_kg = float(input())
cat_food_daily_kg = float(input())
turtle_food_daily_grams = float(input())

total_food_needed = (dog_food_daily_kg + cat_food_daily_kg + (turtle_food_daily_grams / 1000)) * days

if total_food_needed <= total_food_kg:
    food_left = total_food_kg - total_food_needed
    print(f'{floor(food_left)} kilos of food left.')
else:
    food_not_enough = total_food_needed - total_food_kg
    print(f'{ceil(food_not_enough)} more kilos of food are needed.')