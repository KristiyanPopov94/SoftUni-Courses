first_word = input()
second_word = input()
previous_string = first_word

for letter in range(len(first_word)):
    # if first_word[index] != second_word[index]:
    #     first_word = second_word[:index + 1] + first_word[index + 1:]
    #     print(first_word)
    left_part = second_word[:letter + 1]
    right_part = first_word[letter + 1:]
    new_string = left_part + right_part

    if new_string != previous_string:
        print(new_string)
        previous_string = new_string