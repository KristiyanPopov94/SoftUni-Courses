fund_to_be_raised = int(input())

cash_payment = 0
cash_payment_count = 0
card_payment = 0
card_payment_count = 0
money_raised = 0
average_cash = 0
average_card = 0

is_raised = False
counter = 0

command = input()
while command != 'End':
    price = int(command)
    if counter % 2 == 0 and price <= 100:
        cash_payment += price
        cash_payment_count += 1
        print('Product sold!')
    elif counter % 2 == 1 and price >= 10:
        card_payment += price
        card_payment_count += 1
        print('Product sold!')
    else:
        print('Error in transaction!')

    money_raised = cash_payment + card_payment

    if money_raised >= fund_to_be_raised:
        is_raised = True
        break

    counter += 1
    command = input()

if cash_payment_count > 0:
    average_cash = cash_payment / cash_payment_count
if card_payment_count > 0:
    average_card = card_payment / card_payment_count

if is_raised:
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_card:.2f}')
else:
    print('Failed to collect required money for charity.')