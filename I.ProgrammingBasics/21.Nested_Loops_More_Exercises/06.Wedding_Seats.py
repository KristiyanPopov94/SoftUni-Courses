sectors = input()
rows = int(input())
odd_spots = int(input())
counter = 0

for sector in range(ord('A'), ord(sectors) + 1):
    for row in range(1, rows + 1):
        if row % 2 == 1:
            for spot in range(ord('a'), ord('a') + (odd_spots)):
                counter += 1
                print(f'{chr(sector)}{row}{chr(spot)}')
        else:
            for spot in range(ord('a'), ord('a') + (odd_spots + 2)):
                counter += 1
                print(f'{chr(sector)}{row}{chr(spot)}')
    rows += 1
print(counter)