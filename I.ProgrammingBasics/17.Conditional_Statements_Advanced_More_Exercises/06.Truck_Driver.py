season = input()
kilometers_a_month = float(input())

price_for_km = 0

if kilometers_a_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price_for_km = 0.75
    elif season == 'Summer':
        price_for_km = 0.90
    elif season == 'Winter':
        price_for_km = 1.05
elif kilometers_a_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price_for_km = 0.95
    elif season == 'Summer':
        price_for_km = 1.10
    elif season == 'Winter':
        price_for_km = 1.25
elif kilometers_a_month <= 20000:
    price_for_km = 1.45

price_before_taxes = kilometers_a_month * price_for_km * 4
total_price = price_before_taxes * (1 - 0.10)

print(f'{total_price:.2f}')