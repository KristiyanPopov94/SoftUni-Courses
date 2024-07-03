contract_length = input()
type_of_contract = input()
mobile_internet = input()
months_to_pay = int(input())

price_for_month = 0

if contract_length == 'one':
    if type_of_contract == 'Small':
        price_for_month = 9.98
    elif type_of_contract == 'Middle':
        price_for_month = 18.99
    elif type_of_contract == 'Large':
        price_for_month = 25.98
    elif type_of_contract == 'ExtraLarge':
        price_for_month = 35.99
elif contract_length == 'two':
    if type_of_contract == 'Small':
        price_for_month = 8.58
    elif type_of_contract == 'Middle':
        price_for_month = 17.09
    elif type_of_contract == 'Large':
        price_for_month = 23.59
    elif type_of_contract == 'ExtraLarge':
        price_for_month = 31.79

if mobile_internet == 'yes':
    if price_for_month <= 10:
        price_for_month += 5.50
    elif price_for_month <= 30:
        price_for_month += 4.35
    elif price_for_month > 30:
        price_for_month += 3.85

total_sum = price_for_month * months_to_pay
if contract_length == 'two':
    total_sum *= (1 - (3.75 / 100))

print(f'{total_sum:.2f} lv.')