cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_length * cake_width

enough_cake = False
while cake_pieces > 0:
    pieces_taken = input()

    if pieces_taken == 'STOP':
        enough_cake = True
        break

    cake_pieces -= int(pieces_taken)

if enough_cake:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
