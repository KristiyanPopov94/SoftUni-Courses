type_of_flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0

if type_of_flowers == 'Roses':
    price = 5
    if flowers_count > 80:
        price *= 0.90
elif type_of_flowers == 'Dahlias':
    price = 3.80
    if flowers_count > 90:
        price *= 0.85
elif type_of_flowers == 'Tulips':
    price = 2.80
    if flowers_count > 80:
        price *= 0.85
elif type_of_flowers == 'Narcissus':
    price = 3
    if flowers_count < 120:
        price *= 1.15
elif type_of_flowers == 'Gladiolus':
    price = 2.50
    if flowers_count < 80:
        price *= 1.20

total_price = price * flowers_count

if budget >= total_price:
    print(f'Hey, you have a great garden with {flowers_count} {type_of_flowers} and'
          f' {(budget - total_price):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total_price - budget):.2f} leva more.')
