start_of_loop = int(input())
end_of_loop = int(input())
special_number = False

for first_number in range(start_of_loop, end_of_loop + 1):
    for second_number in range(start_of_loop, end_of_loop + 1):
        for third_number in range(start_of_loop, end_of_loop + 1):
            for forth_number in range(start_of_loop, end_of_loop + 1):
                if first_number % 2 == 0 and forth_number % 2 == 1:
                    if first_number > forth_number:
                        if (second_number + third_number) % 2 == 0:
                            print(f'{first_number}{second_number}{third_number}{forth_number}', end= ' ')
                elif first_number % 2 == 1 and forth_number % 2 == 0:
                    if first_number > forth_number:
                        if (second_number + third_number) % 2 == 0:
                            print(f'{first_number}{second_number}{third_number}{forth_number}', end= ' ')