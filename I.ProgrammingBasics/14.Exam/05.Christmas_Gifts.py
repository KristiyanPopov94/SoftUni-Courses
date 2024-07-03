kids = 0
adults = 0
presents_price_kids = 5
presents_price_adults = 15

command = input()
while command != 'Christmas':
    age = int(command)

    if age <= 16:
        kids += 1
    else:
        adults += 1

    command = input()

total_price_kids = kids * presents_price_kids
total_price_adults = adults * presents_price_adults

print(f'Number of adults: {adults}')
print(f'Number of kids: {kids}')
print(f'Money for toys: {total_price_kids}')
print(f'Money for sweaters: {total_price_adults}')
