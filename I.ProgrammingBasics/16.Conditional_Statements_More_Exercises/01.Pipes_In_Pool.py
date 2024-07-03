pool_volume = int(input())
p1 = int(input())
p2 = int(input())
hours_employee_missing = float(input())

liters_filled = (p1 + p2) * hours_employee_missing
p1_filled = p1 * hours_employee_missing
p2_filled = p2 * hours_employee_missing

percentage_filled = (liters_filled / pool_volume) * 100
p1_percentage_filled = (p1_filled / liters_filled) * 100
p2_percentage_filled = (p2_filled / liters_filled) * 100

if liters_filled > pool_volume:
    excessive_water = liters_filled - pool_volume
    print(f'For {hours_employee_missing:.2f} hours the pool overflows with {excessive_water:.2f} liters.')
else:
    print(f'The pool is {percentage_filled:.2f}% full. Pipe 1: {p1_percentage_filled:.2f}%. Pipe 2: '
          f'{p2_percentage_filled:.2f}%.')
