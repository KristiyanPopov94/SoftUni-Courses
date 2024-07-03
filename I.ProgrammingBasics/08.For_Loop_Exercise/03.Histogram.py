numbers_count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(numbers_count):
    current_number = int(input())

    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

percentage_part = 100 / (p1 + p2 + p3 + p4 + p5)

print(f'{(p1 * percentage_part):.2f}%')
print(f'{(p2 * percentage_part):.2f}%')
print(f'{(p3 * percentage_part):.2f}%')
print(f'{(p4 * percentage_part):.2f}%')
print(f'{(p5 * percentage_part):.2f}%')
