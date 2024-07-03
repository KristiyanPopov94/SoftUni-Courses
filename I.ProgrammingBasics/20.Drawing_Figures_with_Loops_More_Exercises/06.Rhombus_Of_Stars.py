rows = int(input())
current_row = rows

for row1 in range(1, rows + 1):
    for i in range(current_row, 0, -1):
        print(' ', end='')
    for _ in range(0, row1):
        print('*', end='')
    print('')
    current_row -= 1