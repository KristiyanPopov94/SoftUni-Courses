length = float(input())
width = float(input())

length_in_sm = length * 100
width_in_sm = (width - 1) * 100

work_places_a_roll = width_in_sm // 70
rolls = length_in_sm // 120

total_work_places = (work_places_a_roll * rolls) - 3

print(total_work_places)