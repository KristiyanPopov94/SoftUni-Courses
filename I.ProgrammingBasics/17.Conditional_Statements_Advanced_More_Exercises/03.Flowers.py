chrysanthemum_bought = int(input())
roses_bought = int(input())
tulips_bought = int(input())
season = input()
holiday = input()

total_flowers = chrysanthemum_bought + roses_bought + tulips_bought

chrysanthemum_price = 0
roses_price = 0
tulips_price = 0
final_price = 0
discount = 0

if season == 'Spring' or season == 'Summer':
    chrysanthemum_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
    if season == 'Spring' and tulips_bought > 7:
        discount += 0.05
elif season == 'Autumn' or season == 'Winter':
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
    if season == 'Winter' and roses_bought >= 10:
        discount += 0.10

total_price_before_discount = (chrysanthemum_bought * chrysanthemum_price) + \
                              (roses_bought * roses_price) + \
                              (tulips_bought * tulips_price)

if holiday == 'Y':
    total_price_before_discount *= 1.15

if discount > 0:
    total_price = total_price_before_discount * (1 - discount)
else:
    total_price = total_price_before_discount

if total_flowers > 20:
    final_price = (total_price * (1 - 0.20)) + 2
else:
    final_price = total_price + 2

print(f'{final_price:.2f}')