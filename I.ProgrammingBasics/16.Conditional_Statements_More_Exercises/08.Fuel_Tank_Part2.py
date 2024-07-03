type_of_fuel = input()
fuel_liters = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

fuel_price = 0

if type_of_fuel == 'Gasoline':
    fuel_price = gasoline_price
    if club_card == 'Yes':
        club_card_discount = 0.18
        fuel_price -= club_card_discount
elif type_of_fuel == 'Diesel':
    fuel_price = diesel_price
    if club_card == 'Yes':
        club_card_discount = 0.12
        fuel_price -= club_card_discount
elif type_of_fuel == 'Gas':
    fuel_price = gas_price
    if club_card == 'Yes':
        club_card_discount = 0.08
        fuel_price -= club_card_discount

if 20 <= fuel_liters <= 25:
    extra_discount_percent = 0.08
    fuel_price = fuel_price * (1 - extra_discount_percent)
elif fuel_liters > 25:
    extra_discount_percent = 0.1
    fuel_price = fuel_price * (1 - extra_discount_percent)

total_price = fuel_price * fuel_liters
print(f'{total_price:.2f} lv.')