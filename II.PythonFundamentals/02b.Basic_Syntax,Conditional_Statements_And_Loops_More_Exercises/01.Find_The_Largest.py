number = int(input())
max_number = '0'
final_number = number

number_to_string = str(number)

for char in range(len(number)):
    print(int(number_to_string[char]))
    print(max_number[char])
    max_number[char] += number_to_string[char]
    if int(number_to_string[char]) > int(str(max_number[char])):
        max_number = str(number_to_string[char])
print(max_number)
