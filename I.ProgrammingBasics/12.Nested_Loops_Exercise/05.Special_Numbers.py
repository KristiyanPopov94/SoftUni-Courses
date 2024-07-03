num = int(input())
numbers_count = 0

for number in range(1111, 10_000):
    number_to_str = str(number)

    for char in range(len(number_to_str)):
        if int(number_to_str[char]) != 0 and num % int(number_to_str[char]) == 0:
            numbers_count += 1

    if numbers_count == 4:
        print(number, end=" ")

    numbers_count = 0
