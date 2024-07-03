c = 0
n = 0
o = 0

word = ''

command = input()
while command != 'End':
    if c == 1 and n == 1 and o == 1:
        print(f'{word}', end=" ")
        c = 0
        n = 0
        o = 0
        word = ''
        continue

    letter = command

    if letter.isalpha():
        if command == 'c' and c == 0:
            c = 1
            command = input()
            if command == 'End':
                print(f'{word}', end=" ")
            continue
        elif command == 'n' and n == 0:
            n = 1
            command = input()
            if command == 'End':
                print(f'{word}', end=" ")
            continue
        elif command == 'o' and o == 0:
            o = 1
            command = input()
            if command == 'End':
                print(f'{word}', end=" ")
            continue

        word += letter

    command = input()