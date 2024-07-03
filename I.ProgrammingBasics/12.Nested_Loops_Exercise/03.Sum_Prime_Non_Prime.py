command = input()

sum_prime_numbers = 0
sum_nonprime_numbers = 0

while command != 'stop':
    number = int(command)

    if number < 0:
        print('Number is negative.')

    if number > 0:

        for i in range(2, int(number / 2) + 1):

            if (number % i) == 0:
                sum_nonprime_numbers += number
                break
        else:
            sum_prime_numbers += number

    if number == 1:
        sum_nonprime_numbers += 1

    command = input()

print(f'Sum of all prime numbers is: {sum_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_nonprime_numbers}')
