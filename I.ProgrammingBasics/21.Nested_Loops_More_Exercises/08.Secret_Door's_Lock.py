hundreds_upper_level = int(input())
tens_upper_level = int(input())
ones_upper_level = int(input())

hundreds = 0
tens = 0
ones = 0

for hundreds in range(1, hundreds_upper_level + 1):
    for tens in range(1, tens_upper_level + 1):
        for ones in range(1, ones_upper_level + 1):
            if hundreds % 2 == 0 and ones % 2 == 0:
                if tens == 2 or tens == 3 or tens == 5 or tens == 7:
                    print(f'{hundreds} {tens} {ones}')