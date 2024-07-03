from math import floor
from math import ceil

magnolii = int(input())
ziumbiuli = int(input())
roses = int(input())
cactus = int(input())
present_price = float(input())

taxes = 0.05

total_income = ((magnolii * 3.25) + (ziumbiuli * 4) + (roses * 3.5) + (cactus * 8)) * (1 - taxes)

if total_income >= present_price:
    money_left = total_income - present_price
    print(f'She is left with {floor(money_left)} leva.')
else:
    money_not_enough = present_price - total_income
    print(f'She will have to borrow {ceil(money_not_enough)} leva.')