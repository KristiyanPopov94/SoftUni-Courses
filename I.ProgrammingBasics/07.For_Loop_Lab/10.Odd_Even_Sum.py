count_of_numbers = int(input())

even_sum = 0
odd_sum = 0

for number in range(count_of_numbers):
    value = int(input())
    if number % 2 == 0:
        even_sum += value
    else:
        odd_sum += value

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum - odd_sum)}')
