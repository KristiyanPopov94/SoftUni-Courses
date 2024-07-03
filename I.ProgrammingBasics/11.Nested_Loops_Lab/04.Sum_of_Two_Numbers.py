iteration_start = int(input())
iteration_end = int(input())
magical_number = int(input())
combination_found = False

counter = 0
number1 = 0
number2 = 0

for number1 in range(iteration_start, iteration_end + 1):
    for number2 in range(iteration_start, iteration_end + 1):

        counter += 1

        if number1 + number2 == magical_number:
            combination_found = True
            break

    if combination_found:
        break

if combination_found:
    print(f'Combination N:{counter} ({number1} + {number2} = {magical_number})')
else:
    print(f'{counter} combinations - neither equals {magical_number}')
