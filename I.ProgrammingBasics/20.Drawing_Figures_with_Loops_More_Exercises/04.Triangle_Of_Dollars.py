count = int(input())

for row in range(1, count + 1):
    for col in range(1, row + 1):
        print('$', end=" ")
    print()