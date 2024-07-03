from sys import maxsize

pairs_count = int(input())

previous_pair = 0
current_pair = 0
max_difference = -maxsize

not_a_pair = False
if_first_pair = True

for i in range(0, pairs_count):
    for u in range(0, 2):
        number = int(input())
        current_pair += number

        if u == 1 and if_first_pair:
            previous_pair = current_pair
            if_first_pair = False

        if u % 2 == 1:
            if current_pair != previous_pair:
                if abs(current_pair - previous_pair) > max_difference:
                    max_difference = abs(current_pair - previous_pair)

    if previous_pair != current_pair and i > 0:
        not_a_pair = True

    previous_pair = current_pair
    current_pair = 0

if not_a_pair:
    print(f'No, maxdiff={max_difference}')
else:
    print(f'Yes, value={previous_pair}')