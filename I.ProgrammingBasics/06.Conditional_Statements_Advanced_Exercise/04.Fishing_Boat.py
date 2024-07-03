budget = int(input())
season = input()
fisherman_count = int(input())

price = 0
discount = 0

if season == 'Spring':
    price = 3000
elif season == 'Winter':
    price = 2600
elif season == 'Summer' or season == 'Autumn':
    price = 4200

if fisherman_count <= 6:
    discount = 0.1
elif fisherman_count <= 11:
    discount = 0.15
elif fisherman_count >= 12:
    discount = 0.25

final_price = price * (1 - discount)

if fisherman_count % 2 == 0 and season != 'Autumn':
    final_price *= 0.95

if budget >= final_price:
    print(f'Yes! You have {(budget - final_price):.2f} leva left.')
else:
    print(f'Not enough money! You need {(final_price - budget):.2f} leva.')
