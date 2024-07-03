command = input()
total_coffees_needed = 0

while command != 'END':
    if command.lower() == 'coding' or \
            command.lower() == 'dog' or \
            command.lower() == 'cat' or \
            command.lower() == 'movie':
        if command.islower():
            total_coffees_needed += 1
        else:
            total_coffees_needed += 2
    command = input()

if total_coffees_needed > 5:
    print('You need extra sleep')
else:
    print(total_coffees_needed)
