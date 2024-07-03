start_of_loop = int(input())
end_of_loop = int(input())
magical_number = int(input())

combinations = 0
is_number_found = False

for first_number in range(start_of_loop, end_of_loop + 1):
    for second_number in range(start_of_loop, end_of_loop + 1):
        combinations += 1

        if first_number + second_number == magical_number:
            print(f'Combination N:{combinations} ({first_number} + {second_number} = {magical_number})')
            is_number_found = True
            exit()
else:
    print(f'{combinations} combinations - neither equals {magical_number}')