n1 = int(input())
n2 = int(input())
operator = input()
odd_or_even = ''

if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd_or_even}')
elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd_or_even}')
elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd_or_even}')
elif operator == '/':
    if n1 == 0:
        print(f'Cannot divide {n2} by zero')
    elif n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
        print(f'{n1} / {n2} = {result:.2f}')
elif operator == '%':
    if n1 == 0:
        print(f'Cannot divide {n2} by zero')
    elif n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2
        print(f'{n1} % {n2} = {result}')
