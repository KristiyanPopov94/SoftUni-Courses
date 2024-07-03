orders_count = int(input())
total_price = 0

for _ in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_daily = int(input())

    if 0.01 <= price_per_capsule <= 100 \
            and days in range(1, 31+1) \
            and capsules_needed_daily in range(1, 2000+1):
        price = capsules_needed_daily * price_per_capsule * days
        total_price += price
        print(f'The price for the coffee is: ${price:.2f}')
    else:
        continue
print(f'Total: ${total_price:.2f}')