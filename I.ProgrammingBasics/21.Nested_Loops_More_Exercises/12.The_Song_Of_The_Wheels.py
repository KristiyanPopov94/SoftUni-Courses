control_number = int(input())

counter = 1
password = ''

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if counter == 4:
                    password = str(a) + str(b) + str(c) + str(d)

                if (a * b) + (c * d) == control_number:
                    if a < b:
                        if c > d:
                            counter += 1
                            print(f'{a}{b}{c}{d}', end=' ')
print()
if password != '':
    print(f'Password: {password}')
else:
    print('No!')
