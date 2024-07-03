money_saved = 0

command = input()
while command != 'End':
    destination = command
    money_needed = float(input())

    money_saved += float(input())
    while money_saved < money_needed:
        money_saved += float(input())

    print(f'Going to {destination}!')
    money_saved = 0
    command = input()
