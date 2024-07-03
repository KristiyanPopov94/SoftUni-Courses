month = input()
nights_to_stay = int(input())
apartment_price = 0
studio_price = 0
discount_for_studio = 0
discount_for_apartment = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if nights_to_stay > 14:
        discount_for_studio = 0.30
    elif nights_to_stay > 7:
        discount_for_studio = 0.05
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights_to_stay > 14:
        discount_for_studio = 0.20
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if nights_to_stay > 14:
    discount_for_apartment = 0.10

if discount_for_apartment > 0:
    final_price_apartment = apartment_price * nights_to_stay
    print(f'Apartment: {(final_price_apartment - final_price_apartment * discount_for_apartment):.2f} lv.')
else:
    print(f'Apartment: {(apartment_price * nights_to_stay):.2f} lv.')

if discount_for_studio > 0:
    final_price_studio = studio_price * nights_to_stay
    print(f'Studio: {(final_price_studio - final_price_studio * discount_for_studio):.2f} lv.')
else:
    print(f'Studio: {(studio_price * nights_to_stay):.2f} lv.')
