import sys

count_of_numbers = int(input())

sum_of_numbers = 0
max_number = -sys.maxsize

for number in range(count_of_numbers):
    current_number = int(input())
    sum_of_numbers += current_number
    if current_number > max_number:
        max_number = current_number

if max_number == sum_of_numbers - max_number:
    print('Yes')
    print('Sum =', max_number)
else:
    print("No")
    sum_of_numbers = sum_of_numbers - max_number
    print(f'Diff = {abs(max_number - sum_of_numbers)}')
