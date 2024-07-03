inherited_money = float(input())
year_to_live_up_to = int(input())

money_spend = 0
age = 18
money_not_enough = False

for year in range (1800, year_to_live_up_to + 1):
    if year % 2 == 0:
        money_spend += 12000
    else:
        money_spend += 12000 + (50 * age)

    if money_spend > inherited_money:
        money_not_enough = True

    age += 1

if money_not_enough:
    insufficient_money = money_spend - inherited_money
    print(f'He will need {insufficient_money:.2f} dollars to survive.')
else:
    money_left = inherited_money - money_spend
    print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')