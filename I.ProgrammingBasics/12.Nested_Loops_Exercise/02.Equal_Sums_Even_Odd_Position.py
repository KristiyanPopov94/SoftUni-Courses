first_number = int(input())
second_number = int(input())

sum_even = 0
sum_odd = 0

for number in range(first_number, second_number + 1):
    number_to_str = str(number)

    for char in range(len(number_to_str)):

        if char % 2 == 0:
            sum_even += int(number_to_str[char])
        else:
            sum_odd += int(number_to_str[char])

    if sum_even == sum_odd:
        print(number, end=" ")

    sum_even = 0
    sum_odd = 0
