bottles_bought = int(input())

detergent_ml = bottles_bought * 750
ml_used = 0
counter = 1

plates_washed = 0
pots_washed = 0
is_not_enough = False

command = input()
while command != 'End':
    dishes = int(command)

    if counter < 3:
        plates_washed += dishes
    else:
        pots_washed += dishes
        counter = 0

    ml_used = (plates_washed * 5) + (pots_washed * 15)

    if ml_used > detergent_ml:
        is_not_enough = True
        break

    counter += 1
    command = input()

if is_not_enough:
    detergent_not_enough = ml_used - detergent_ml
    print(f'Not enough detergent, {detergent_not_enough} ml. more necessary!')
else:
    detergent_left = detergent_ml - ml_used
    print('Detergent was enough!')
    print(f'{plates_washed} dishes and {pots_washed} pots were washed.')
    print(f'Leftover detergent {detergent_left} ml.')