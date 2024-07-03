floors = int(input())
rooms = int(input())

top_floor = floors
for floor in range(floors, 0, -1):
    for room in range(rooms):

        if floor == top_floor:
            print(f'L{top_floor}{room}', end=" ")
        elif floor % 2 == 0:
            print(f'O{floor}{room}', end=" ")
        elif floor % 2 != 0:
            print(f'A{floor}{room}', end=" ")

    print('')
