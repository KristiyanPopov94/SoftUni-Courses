# · Premiere - премиерна прожекция, на цена 12.00 лева;
# · Normal - стандартна прожекция, на цена 7.50 лева;
# · Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

type_of_projection = input()
rolls = int(input())
columns = int(input())

total_seats = rolls * columns
total_profit = 0

if type_of_projection == 'Premiere':
    total_profit = total_seats * 12
elif type_of_projection == 'Normal':
    total_profit = total_seats * 7.5
elif type_of_projection == 'Discount':
    total_profit = total_seats * 5

print(f'{total_profit:.2f} leva')
