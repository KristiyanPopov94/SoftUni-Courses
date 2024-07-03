budget = float(input())
extras = int(input())
price_for_clothing_of_extras = float(input())

# · Декорът за филма е на стойност 10% от бюджета.
# · При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

if extras > 150:
    price_for_clothing_of_extras *= 0.90

expenses = extras * price_for_clothing_of_extras + budget * 0.10

if expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {(expenses - budget):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {(budget - expenses):.2f} leva left.')
