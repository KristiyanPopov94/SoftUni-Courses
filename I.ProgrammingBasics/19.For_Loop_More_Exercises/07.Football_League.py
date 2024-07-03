capacity = int(input())
fans_count = int(input())

sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for _ in range(0, fans_count):
    sector_to_be = input()

    if sector_to_be == 'A':
        sector_A += 1
    elif sector_to_be == 'B':
        sector_B += 1
    elif sector_to_be == 'V':
        sector_V += 1
    elif sector_to_be == 'G':
        sector_G += 1

percent_sector_A = sector_A / fans_count * 100
percent_sector_B = sector_B / fans_count * 100
percent_sector_V = sector_V / fans_count * 100
percent_sector_G = sector_G / fans_count * 100
total_percent_fans = (sector_A + sector_B + sector_V + sector_G) / capacity * 100

print(f'{percent_sector_A:.2f}%')
print(f'{percent_sector_B:.2f}%')
print(f'{percent_sector_V:.2f}%')
print(f'{percent_sector_G:.2f}%')
print(f'{total_percent_fans:.2f}%')