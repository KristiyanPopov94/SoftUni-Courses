vacation_days = int(input())
type_of_room = input()
remark = input()

total_price = 0
discount = 0

if type_of_room == 'room for one person':
    total_price = 18.00 * (vacation_days - 1)
elif type_of_room == 'apartment':
    if vacation_days < 10:
        discount = 0.30
    elif vacation_days <= 15:
        discount = 0.35
    else:
        discount = 0.50
    total_price = 25.00 * (vacation_days - 1)
elif type_of_room == 'president apartment':
    if vacation_days < 10:
        discount = 0.10
    elif vacation_days <= 15:
        discount = 0.15
    else:
        discount = 0.20
    total_price = 35.00 * (vacation_days - 1)

final_price = total_price * (1 - discount)

if remark == 'positive':
    final_price *= 1.25
else:
    final_price *= 0.90

print(f'{final_price:.2f}')
