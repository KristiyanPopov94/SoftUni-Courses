account_input = input()
total_sum = 0

if account_input == 'NoMoreMoney':
    pass
elif float(account_input) < 0:
    print('Invalid operation!')
else:
    total_sum = float(account_input)
    print(f'Increase: {total_sum:.2f}')
    while True:
        new_input = input()

        if new_input == 'NoMoreMoney':
            break
        elif float(new_input) < 0:
            print('Invalid operation!')
            break

        print(f'Increase: {float(new_input):.2f}')
        total_sum += float(new_input)

print(f'Total: {total_sum:.2f}')
