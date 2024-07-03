kilometers = int(input())
part_of_day = input()

taxi_starting_price = 0.70
taxi_price_day = 0.79
taxi_price_night = 0.90
bus_price = 0.09
train_price = 0.06

price = 0
if kilometers < 20:
    if part_of_day == 'day':
        price = taxi_starting_price + (kilometers * taxi_price_day)
    else:
        price = taxi_starting_price + (kilometers * taxi_price_night)
elif kilometers < 100:
    price = kilometers * bus_price
elif kilometers >= 100:
    price = kilometers * train_price

print(f'{price:.2f}')