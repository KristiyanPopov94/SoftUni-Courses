#                                       Morning                                  Afternoon                                           Evening
# 10 <= градуси <= 18        Outfit = Sweatshirt Shoes = Sneakers       Outfit = Shirt     Shoes = Moccasins             Outfit = Shirt Shoes = Moccasins
# 18 < градуси <= 24         Outfit = Shirt Shoes = Moccasins           Outfit = T-Shirt   Shoes = Sandals               Outfit = Shirt Shoes = Moccasins
# градуси >= 25              Outfit = T-Shirt Shoes = Sandals           Outfit = Swim Suit Shoes = Barefoot              Outfit = Shirt Shoes = Moccasins

degrees = int(input())
part_of_the_day = input()
outfit = ''
shoes = ''


if part_of_the_day == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif part_of_the_day == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif part_of_the_day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')
