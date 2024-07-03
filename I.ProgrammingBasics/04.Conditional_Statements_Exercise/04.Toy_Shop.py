# · Пъзел - 2.60 лв.
# · Говореща кукла - 3 лв.
# · Плюшено мече - 4.10 лв.
# · Миньон - 8.20 лв.
# · Камионче - 2 лв.

vacation_price = float(input())
puzzels = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_count_of_toys = puzzels + talking_dolls + teddy_bears + minions + trucks
total_price = puzzels * 2.60 + talking_dolls * 3 + teddy_bears * 4.10 + minions * 8.20 + trucks * 2

if total_count_of_toys >= 50:
    total_price *= 0.75

money_earned = total_price * 0.90

# Ако парите са достатъчни се отпечатва:
#      "Yes! {оставащите пари} lv left."

# · Ако парите НЕ са достатъчни се отпечатва:
#      "Not enough money! {недостигащите пари} lv needed."

if money_earned >= vacation_price:
    print(f'Yes! {(money_earned - vacation_price):.2f} lv left.')
else:
    print(f'Not enough money! {(vacation_price - money_earned):.2f} lv needed.')
