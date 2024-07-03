total_cats = int(input())
counter = 0

g1_small_cats = 0
g2_large_cats = 0
g3_huge_cats = 0
total_food_in_grams = 0

while counter < total_cats:

    food_eaten = float(input())
    total_food_in_grams += food_eaten
    counter += 1

    if 100 <= food_eaten < 200:
        g1_small_cats += 1
    elif 200 <= food_eaten < 300:
        g2_large_cats += 1
    elif 300 <= food_eaten < 400:
        g3_huge_cats += 1

total_food_price = (total_food_in_grams / 1000) * 12.45

print(f'Group 1: {g1_small_cats} cats.')
print(f'Group 2: {g2_large_cats} cats.')
print(f'Group 3: {g3_huge_cats} cats.')
print(f'Price for food per day: {total_food_price:.2f} lv.')
