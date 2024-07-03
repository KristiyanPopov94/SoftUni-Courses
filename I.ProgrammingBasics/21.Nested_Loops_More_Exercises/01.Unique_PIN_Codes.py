first_number_upper_limit = int(input())
second_number_upper_limit = int(input())
third_number_upper_limit = int(input())

first_number = 0
second_number = 0
third_number = 0

for first_number in range(1, first_number_upper_limit + 1):
    for second_number in range(1, second_number_upper_limit + 1):
        for third_number in range(1, third_number_upper_limit + 1):
            if first_number % 2 == 0 and third_number % 2 == 0:
                if second_number == 2 or second_number == 3 or second_number == 5 or second_number == 7:
                    print(f'{first_number} {second_number} {third_number}')