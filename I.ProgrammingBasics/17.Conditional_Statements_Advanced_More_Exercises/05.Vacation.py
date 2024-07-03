budget = float(input())
season = input()

holiday_location = ''
accommodation_type = ''
holiday_price = 0


if season == 'Summer':
    holiday_location = 'Alaska'
elif season == 'Winter':
    holiday_location = 'Morocco'

if budget <= 1000:
    accommodation_type = 'Camp'
    if season == 'Summer':
        holiday_price = budget * 0.65
    elif season == 'Winter':
        holiday_price = budget * 0.45
elif budget <= 3000:
    accommodation_type = 'Hut'
    if season == 'Summer':
        holiday_price = budget * 0.80
    elif season == 'Winter':
        holiday_price = budget * 0.60
elif budget > 3000:
    accommodation_type = 'Hotel'
    holiday_price = budget * 0.90

print(f'{holiday_location} - {accommodation_type} - {holiday_price:.2f}')