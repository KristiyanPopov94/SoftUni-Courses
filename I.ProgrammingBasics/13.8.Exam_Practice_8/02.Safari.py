budget = float(input())
liters_needed = float(input())
week_day = input()
tour_guide = 100

fuel_price = liters_needed * 2.10
total_price = fuel_price + tour_guide

if week_day == "Saturday":
    discount = 0.10
    total_price = total_price * (1 - discount)
else:
    discount = 0.20
    total_price = total_price * (1 - discount)

if budget >= total_price:
    print(f'Safari time! Money left: {(budget - total_price):.2f} lv.')
else:
    print(f'Not enough money! Money needed: {(total_price - budget):.2f} lv.')