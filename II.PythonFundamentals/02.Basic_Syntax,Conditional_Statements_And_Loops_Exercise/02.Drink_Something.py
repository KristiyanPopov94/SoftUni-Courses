age = int(input())
drink = ''
# if age <= 14:
#     print('drink toddy')
# elif age <= 18:
#     print('drink coke')
# elif age <= 21:
#     print('drink beer')
# else:
#     print('drink whisky')

if age <= 14:
    drink = 'toddy'
elif age <= 18:
    drink = 'coke'
elif age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print('drink', drink)