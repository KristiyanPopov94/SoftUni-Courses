count_of_numbers = int(input())

first_sum = 0
second_sum = 0

for number in range(count_of_numbers * 2):
    value = int(input())
    if number < count_of_numbers:
        first_sum += value
    else:
        second_sum += value

if first_sum == second_sum:
    print(f'Yes, sum = {first_sum}')
else:
    print(f'No, diff = {abs(first_sum - second_sum)}')
