number = int(input())
sum_of_numbers = 0

for i in range (0, number):
    sum_of_numbers += int(input())

average = sum_of_numbers / number

print(f'{average:.2f}')