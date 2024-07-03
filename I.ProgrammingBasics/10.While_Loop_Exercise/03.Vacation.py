vacation_price = float(input())
available_sum = float(input())

days_spending = 0
days_passed = 0

while available_sum < vacation_price and days_spending < 5:
    type_of_transaction = input()
    sum_of_transaction = float(input())
    days_passed += 1

    if type_of_transaction == 'save':
        available_sum += sum_of_transaction
        days_spending = 0
    elif type_of_transaction == 'spend':
        available_sum -= sum_of_transaction
        days_spending += 1
        if available_sum < 0:
            available_sum = 0

if available_sum < vacation_price:
    print(f'You can\'t save the money.')
    print(f'{days_passed}')
else:
    print(f'You saved the money for {days_passed} days.')
