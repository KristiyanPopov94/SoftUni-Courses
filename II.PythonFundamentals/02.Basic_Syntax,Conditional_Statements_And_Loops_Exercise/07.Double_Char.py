strings = input()

while strings != 'End':
    if strings == 'SoftUni':
        strings = input()
        continue

    for letter in strings:
        print(letter * 2, end='')

    print('')
    strings = input()