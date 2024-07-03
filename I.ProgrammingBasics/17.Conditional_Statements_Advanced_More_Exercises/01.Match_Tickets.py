budget = float(input())
category = input()
peoples_count = int(input())

price_per_ticket = 0
transport_percentage_from_budget = 0

if category == 'VIP':
    price_per_ticket = 499.99
elif category == 'Normal':
    price_per_ticket = 249.99

if peoples_count <= 4:
    transport_percentage_from_budget = 0.75
elif peoples_count <= 9:
    transport_percentage_from_budget = 0.60
elif peoples_count <= 24:
    transport_percentage_from_budget = 0.50
elif peoples_count <= 49:
    transport_percentage_from_budget = 0.40
elif peoples_count >= 50:
    transport_percentage_from_budget = 0.25

money_left_for_tickets = budget * (1 - transport_percentage_from_budget)
total_price = price_per_ticket * peoples_count

if money_left_for_tickets >= total_price:
    money_left = money_left_for_tickets - total_price
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_not_enough = total_price - money_left_for_tickets
    print(f'Not enough money! You need {money_not_enough:.2f} leva.')