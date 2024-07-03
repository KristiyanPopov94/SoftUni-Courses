lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
toys_count = 0
counter = 0

for i in range(1, lily_age + 1):
    if i % 2 != 0:
        toys_count += 1
    else:
        money += 10 + (counter * 10) - 1
        counter += 1

total_money = toys_count * toy_price + money

if total_money >= washing_machine_price:
    money_left = total_money - washing_machine_price
    print(f'Yes! {money_left:.2f}')
else:
    money_needed = washing_machine_price - total_money
    print(f'No! {money_needed:.2f}')
