target_number = int(input())

is_bigger_than_target = False
current_number = 1

for row in range(1, target_number + 1):
    for number_on_row in range(1, row + 1):

        if current_number > target_number:
            is_bigger_than_target = True
            break

        print(current_number, end=" ")
        current_number += 1

    if is_bigger_than_target:
        break

    print('')
