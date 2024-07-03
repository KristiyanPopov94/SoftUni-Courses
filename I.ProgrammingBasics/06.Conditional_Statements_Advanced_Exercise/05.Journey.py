budget = float(input())
season = input()

# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи. Ако е лято ще почива на къмпинг,
# а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел.
# Всеки къмпинг или хотел, според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:

# · При 100 лв. или по-малко - някъде в България:
# o Лято - 30% от бюджета;
# o Зима - 70% от бюджета.

# · При 1000 лв. или по малко - някъде на Балканите:
# o Лято - 40% от бюджета;
# o Зима - 80% от бюджета.

# · При повече от 1000 лв. - някъде из Европа:
# o При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
money_spend = 0
type_of_holiday = ''
place_for_holiday = ''

if budget <= 100:
    if season == 'summer':
        money_spend = budget * 0.30
        type_of_holiday = 'Camp'
    elif season == 'winter':
        money_spend = budget * 0.70
        type_of_holiday = 'Hotel'
    place_for_holiday = 'Bulgaria'
elif budget <= 1000:
    if season == 'summer':
        money_spend = budget * 0.40
        type_of_holiday = 'Camp'
    elif season == 'winter':
        money_spend = budget * 0.80
        type_of_holiday = 'Hotel'
    place_for_holiday = 'Balkans'
else:
    type_of_holiday = 'Hotel'
    money_spend = budget * 0.90
    place_for_holiday = "Europe"

print('Somewhere in ' + place_for_holiday)
print(f'{type_of_holiday} - {money_spend:.2f}')
