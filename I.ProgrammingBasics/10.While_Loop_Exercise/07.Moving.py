width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

area = width_free_space * length_free_space * height_free_space

is_enough_space = False
while area > 0:
    boxes = input()

    if boxes == 'Done':
        is_enough_space = True
        break

    area -= int(boxes)

if is_enough_space:
    print(f'{area} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(area)} Cubic meters more.')
