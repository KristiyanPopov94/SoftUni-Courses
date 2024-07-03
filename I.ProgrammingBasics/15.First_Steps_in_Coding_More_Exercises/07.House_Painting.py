house_height = float(input())
house_wall_length = float(input())
house_roof_height = float(input())

door_area = 1.2 * 2
window_area = 1.5 * 1.5

square_area_total = ((house_height * house_height) * 2) - door_area
rectangle_house_area_total = ((house_height * house_wall_length) - window_area) * 2

rectangle_roof_area_total = (house_height * house_wall_length) * 2
triangle_area_total = ((house_height * house_roof_height) / 2) * 2

liters_green_paint = (square_area_total + rectangle_house_area_total) / 3.4
liters_red_paint = (rectangle_roof_area_total + triangle_area_total) / 4.3

print(f'{liters_green_paint:.2f}')
print(f'{liters_red_paint:.2f}')