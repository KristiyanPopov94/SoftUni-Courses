count = int(input())

for row in range(1, count + 1):

    if row == 1 or row == count:
        print('+', end=' ')
    else:
        print('|', end=' ')

    for column in range(1, count - 1):
        print('-', end=' ')

    if row == 1 or row == count:
        print('+', end='')
    else:
        print('|', end='')

    print('')