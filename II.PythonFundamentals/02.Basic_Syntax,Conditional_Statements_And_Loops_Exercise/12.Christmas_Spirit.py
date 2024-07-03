quantity_of_decorations = int(input())
days_to_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

total_spirit_points = 0
total_cost = 0

for current_day in range(1, days_to_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += quantity_of_decorations * ornament_set_price
        total_spirit_points += ornament_set_points
    if current_day % 3 == 0:
        total_cost += quantity_of_decorations * (tree_skirt_price + tree_garland_price)
        total_spirit_points += tree_skirt_points + tree_garland_points
    if current_day % 5 == 0:
        total_cost += quantity_of_decorations * tree_lights_price
        total_spirit_points += tree_lights_points
        if current_day % 3 == 0:
            total_spirit_points += 30
    if current_day % 10 == 0:
        total_spirit_points -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days_to_christmas % 10 == 0:
    total_spirit_points -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit_points}')