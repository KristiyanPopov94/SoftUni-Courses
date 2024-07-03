fuel_type = input()
liters_left_in_reservoir = int(input())

if liters_left_in_reservoir >= 25:
    if fuel_type == 'Diesel' or fuel_type == 'Gasoline' or fuel_type == 'Gas':
        print(f'You have enough {str.lower(fuel_type)}.')
    else:
        print('Invalid fuel!')
else:
    if fuel_type == 'Diesel' or fuel_type == 'Gasoline' or fuel_type == 'Gas':
        print(f'Fill your tank with {str.lower(fuel_type)}!')
    else:
        print('Invalid fuel!')
