one_leva_coins = int(input())
two_leva_coins = int(input())
five_leva_banknote = int(input())
sum_to_be_paid = int(input())

for one_leva in range(0, one_leva_coins + 1):
    for two_leva in range(0, two_leva_coins + 1):
        for five_leva in range(0, five_leva_banknote + 1):
            sum_of_change = (one_leva * 1) + (two_leva * 2) + (five_leva * 5)

            if sum_of_change == sum_to_be_paid:
                print(f'{one_leva} * 1 lv. + {two_leva} * 2 lv. + {five_leva} * 5 lv. = {sum_to_be_paid} lv.')