from sys import maxsize

numbers_count = int(input())

odd_sum = 0
even_sum = 0

odd_max = -maxsize
odd_min = maxsize
even_max = -maxsize
even_min = maxsize

for i in range(1, numbers_count + 1):
    number = float(input())

    if i % 2 == 1:
        odd_sum += number

        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
    else:
        even_sum += number

        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number

print(f'OddSum={odd_sum:.2f},')
if odd_min != 0 and odd_min != maxsize:
    print(f'OddMin={odd_min:.2f},')
else:
    print(f'OddMin=No,')
if odd_max != 0 and odd_max != -maxsize:
    print(f'OddMax={odd_max:.2f},')
else:
    print(f'OddMax=No,')
print(f'EvenSum={even_sum:.2f},')
if even_min != 0 and even_min != maxsize:
    print(f'EvenMin={even_min:.2f},')
else:
    print(f'EvenMin=No,')
if even_max != 0 and even_max != -maxsize:
    print(f'EvenMax={even_max:.2f}')
else:
    print(f'EvenMax=No')