budget = float(input())

products_bought = 0
sum_spent = 0
money_left = budget
counter = 1
enough_money = True

command = input()
while command != 'Stop':
    product_price = float(input())

    if counter == 3:
        product_price *= 0.5
        counter = 0

    if money_left - product_price < 0:
        print('You don\'t have enough money!')
        print(f'You need {(product_price - money_left):.2f} leva!')
        enough_money = False
        break
    else:
        money_left -= product_price

    products_bought += 1
    sum_spent += product_price
    counter += 1
    command = input()

if enough_money:
    print(f'You bought {products_bought} products for {sum_spent:.2f} leva.')